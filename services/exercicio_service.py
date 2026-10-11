from modules.exercicio import Exercicio

class ExercicioService:
    def __init__(self, repository):
        self.repository = repository
        
    def cadastrar_treino(self, nome, series, repeticoes, id_treino):
        exercicio = Exercicio(None, nome, series, repeticoes, id_treino)
        
        exercicios = self.repository.inserir(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id_treino)
        
        return exercicios
    
    def buscar_por_id(self, id_treino):
        exercicios = self.repository.listar_por_id(id_treino)
        
        return exercicios
    
    def atualizar(self, nome, series, repeticoes, id):
        exercicio = Exercicio(id, nome, series, repeticoes, 1)
        
        exercicios = self.repository.atualizar(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id)
        
        return exercicios
    
    def deletar(self, id):
        exercicio = self.repository.deletar(id)
        
        return exercicio