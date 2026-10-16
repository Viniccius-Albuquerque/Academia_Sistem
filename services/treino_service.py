from modules.treino import Treino, TreinoCreate, TreinoUpdate, TreinoDelete
from services.exercicio_service import ExercicioService
from repositories.exercicio_repository import ExercicioRepository

repositoryE = ExercicioRepository()
serviceE = ExercicioService(repositoryE)

class TreinoService:
    def __init__(self, repository):
        self.repository = repository
        
    def cadastrar_treino(self, nome, dia_semana, id_aluno):
        treino = TreinoCreate(nome, dia_semana, id_aluno)
        verificacao = self.buscar_por_id(id_aluno)
        if verificacao == []:
            return 0
        else:
            if treino.dia_semana in ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]:
                treinos = self.repository.inserir(treino.nome, treino.dia_semana, treino.id_aluno)
                return treinos
            else:
                return -1
    
    def buscar_por_id(self, id):
        treinos = self.repository.listar_por_id(id)
        
        return treinos

    def atualizar(self, dia_semana, nome, id_aluno):
        treino = TreinoUpdate(nome, dia_semana, id_aluno)
        verificacao = self.buscar_por_id(id_aluno)
        if verificacao == []:
            return 0
        if treino.dia_semana in ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]:
            treinos = self.repository.atualizar(treino.dia_semana, treino.nome, treino.id_aluno)
            return treinos
        else:
            return -1
    
    def deletar(self, dia_semana, id_aluno):
        treino = TreinoDelete(dia_semana, id_aluno)

        verificacao = self.buscar_por_id(id_aluno)
        if verificacao == [] or verificacao == None:
            return -1
        for tabelaTreino in verificacao:
            if tabelaTreino["dia_semana"] == dia_semana:
                listaTreino = serviceE.buscar_por_id(tabelaTreino["id"])
                if listaTreino != []:
                    for exercicio in listaTreino:
                        serviceE.deletar(exercicio["id"])
        if treino.dia_semana in ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]:
            treinos = self.repository.deletar(dia_semana, id_aluno)
            return treinos
        else:
            return -2