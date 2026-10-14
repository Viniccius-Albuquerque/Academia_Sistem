from database.conexao import Conectar
from psycopg.rows import dict_row

class TreinoRepository:
    def inserir(self, nome, dia_semana, id_aluno):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    INSERT INTO treino (nome, dia_semana, id_aluno)
                    VALUES (%s, %s, %s)
                    RETURNING id, nome, dia_semana, id_aluno
                ''',
                (nome, dia_semana, id_aluno)
            )
            
            treino = cursor.fetchone()
            
            conexao.commit()
            
            return treino
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
            
    def listar_por_id(self, id):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        cursor.execute(
            '''
                SELECT * FROM treino
                WHERE id_aluno = %s
            ''',
            (id,)
        )
        
        treinos = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return treinos
    
    def atualizar(self, dia_semana, nome, id_aluno):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    UPDATE treino
                    SET nome = %s
                    WHERE dia_semana = %s AND id_aluno = %s
                    RETURNING id, nome, dia_semana, id_aluno
                ''',
                (nome, dia_semana, id_aluno)
            )
        
            treino = cursor.fetchone()
            conexao.commit()
            return treino
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
            
    def deletar(self, dia_semana, id_aluno):
        conexao = Conectar.conectar()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                '''
                    DELETE FROM treino
                    WHERE dia_semana = %s AND id_aluno = %s
                ''',
                (dia_semana, id_aluno)
            )
            conexao.commit()
            return True
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()