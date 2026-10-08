from aluno import Aluno

class AlunoService:
    def __init__(self, repository):
        self.repository = repository
        
    def cadastrar(self, nome, idade, plano):
        aluno = Aluno(None, nome, idade, plano, None)
        
        user = self.repository.inserir(aluno.nome, aluno.idade, aluno.plano)
        
        return user
    
    def listar(self):
        users = self.repository.listar()
        
        return users
    
    def atualizar(self, id, idade, plano):
        aluno = Aluno(id, "None", idade, plano, None)
        
        user = self.repository.atualizar(id, aluno.idade, aluno.plano)
        
        return user
    
    def deletar(self, id):
        user = self.repository.deletar(id)
        
        return user
    
    def desativar(self, id):
        user = self.repository.desativar(id)
        
        return user
    
    def ativar(self, id):
            user = self.repository.ativar(id)
            
            return user
        
    def buscar_por_id(self, id):
        user = self.repository.buscar_por_id(id)
        
        return user
    
    def buscar_por_plano(self, plano):
        users = self.repository.buscar_por_plano(plano)
        
        return users