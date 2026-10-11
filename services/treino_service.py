from modules.treino import Treino

class TreinoService:
    def __init__(self, repository):
        self.repository = repository
        
    def cadastrar_treino(self, nome, dia_semana, id_aluno):
        treino = Treino(None, nome, dia_semana, id_aluno)
        
        treinos = self.repository.inserir(treino.nome, treino.dia_semana, treino.id_aluno)
        
        return treinos
    
    def buscar_por_id(self, id):
        treinos = self.repository.listar_por_id(id)
        
        return treinos

    def atualizar(self, dia_semana, nome, id_aluno):
        treino = Treino(None, nome, dia_semana, id_aluno)
        
        treinos = self.repository.atualizar(treino.dia_semana, treino.nome, treino.id_aluno)
        
        return treinos
    
    def deletar(self, dia_semana, id_aluno):
        treino = self.repository.deletar(dia_semana, id_aluno)
        
        return treino