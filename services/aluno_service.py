from modules.aluno import Aluno, AlunoCreate, AlunoUpdate
from services.treino_service import TreinoService
from repositories.treino_repository import TreinoRepository

class AlunoService:
    def __init__(self, repository, treino_service=None):
        self.repository = repository
        self.treino_service = (treino_service if treino_service is not None else TreinoService(TreinoRepository()))
        
    def cadastrar(self, nome, idade, plano):
        aluno = AlunoCreate(nome, idade, plano)
        
        user = self.repository.inserir(aluno.nome, aluno.idade, aluno.plano)
        
        return user
    
    def listar(self):
        users = self.repository.listar()
        
        return users
    
    def atualizar(self, id, idade, plano):
        aluno = AlunoUpdate(id, idade, plano)
        
        user = self.repository.atualizar(id, aluno.idade, aluno.plano)
        
        return user
    
    def deletar(self, id):
        verificacao = self.treino_service.buscar_por_id(id)
        for treino in verificacao:
            self.treino_service.deletar(treino["dia_semana"], id)
        
        user = self.repository.deletar(id)
        
        return user
    
    def desativar(self, id):
        verificacao = self.buscar_por_id(id)
        if verificacao is None:
            return {"mensagem": -1}
        if verificacao["estado"] == "desativado":
            return {"mensagem": 0}
        
        self.repository.desativar(id)
        
        return {"mensagem": 1}
    
    def ativar(self, id):
        verificacao = self.buscar_por_id(id)
        if verificacao is None:
            return {"mensagem": -1}
        if verificacao["estado"] == "ativo":
            return {"mensagem": 0}
        
        self.repository.ativar(id)
            
        return {"mensagem": 1}
        
    def buscar_por_id(self, id):
        user = self.repository.buscar_por_id(id)
        
        return user
    
    def buscar_por_plano(self, plano):
        users = self.repository.buscar_por_plano(plano)
        
        return users