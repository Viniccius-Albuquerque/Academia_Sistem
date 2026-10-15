from database.conexao import Conectar
from psycopg.rows import dict_row

class ExercicioRepository:
    def inserir(self, nome, series, repeticoes, id_treino):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    INSERT INTO exercicio (nome, series, repeticoes, id_treino)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, nome, series, repeticoes, id_treino
                ''',
                (nome, series, repeticoes, id_treino)
            )
            
            exercicio = cursor.fetchone()
            
            conexao.commit()
            
            return exercicio
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
            
    def listar_por_id(self, id_treino):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        cursor.execute(
            '''
                SELECT * FROM exercicio
                WHERE id_treino = %s
            ''',
            (id_treino,)
        )
        
        exercicios = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return exercicios
    
    def atualizar(self, nome, series, repeticoes, id):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    UPDATE exercicio
                    SET nome = %s, series = %s, repeticoes = %s
                    WHERE id = %s
                    RETURNING id, nome, series, repeticoes
                ''',
                (nome, series, repeticoes, id)
            )
        
            exercicio = cursor.fetchone()
            conexao.commit()
            return exercicio
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
            
    def deletar(self, id):
        conexao = Conectar.conectar()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                '''
                    DELETE FROM exercicio
                    WHERE id = %s
                ''',
                (id,)
            )
            conexao.commit()
            return cursor.rowcount
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()