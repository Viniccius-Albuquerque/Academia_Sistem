from database.conexao import Conectar
from psycopg.rows import dict_row

class AlunoRepository:
    def inserir(self, nome, idade, plano):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    INSERT INTO aluno (nome, idade, plano)
                    VALUES (%s, %s, %s)
                    RETURNING id, nome, idade, plano, estado
                ''',
                (nome, idade, plano)
            )
            
            aluno = cursor.fetchone()
            
            conexao.commit()
            
            return aluno
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
        
    def listar(self):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        cursor.execute(
            '''
                SELECT * FROM aluno
            '''
        )
        
        alunos = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return alunos
    
    def atualizar(self, id, idade, plano):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    UPDATE aluno
                    SET idade = %s,
                        plano = %s
                    WHERE id = %s
                    RETURNING id, nome, idade, plano, estado
                ''',
                (idade, plano, id)
            )
        
            aluno = cursor.fetchone()
            conexao.commit()
            return aluno
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
                    DELETE FROM aluno
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
            
    def desativar(self, id):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        try:
            cursor.execute(
                '''
                    UPDATE aluno
                    SET estado = 'desativado'
                    WHERE id = %s
                    RETURNING id, nome, idade, plano, estado
                ''',
                (id, )
            )
        
            aluno = cursor.fetchone()
            conexao.commit()
            return aluno
        except Exception:
            conexao.rollback()
            raise
        finally:
            cursor.close()
            conexao.close()
            
    def ativar(self, id):
            conexao = Conectar.conectar()
            cursor = conexao.cursor(row_factory=dict_row)
            
            try:
                cursor.execute(
                    '''
                        UPDATE aluno
                        SET estado = 'ativo'
                        WHERE id = %s
                        RETURNING id, nome, idade, plano, estado
                    ''',
                    (id, )
                )
            
                aluno = cursor.fetchone()
                conexao.commit()
                return aluno
            except Exception:
                conexao.rollback()
                raise
            finally:
                cursor.close()
                conexao.close()
                
    def buscar_por_id(self, id):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        cursor.execute(
            '''
                SELECT * FROM aluno
                WHERE id = %s
            ''',
            (id,)
        )
        
        aluno = cursor.fetchone()
        
        cursor.close()
        conexao.close()
        
        return aluno
    
    def buscar_por_plano(self, plano):
        conexao = Conectar.conectar()
        cursor = conexao.cursor(row_factory=dict_row)
        
        cursor.execute(
            '''
                SELECT * FROM aluno
                WHERE plano = %s
            ''',
            (plano,)
        )
        
        alunos = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return alunos