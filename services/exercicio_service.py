from modules.exercicio import ExercicioUpdate, ExercicioCreate
from repositories.treino_repository import TreinoRepository

class ExercicioService:
    def __init__(self, repository, treino_repository=None):
        self.repository = repository
        self.treino_repository = (treino_repository if treino_repository is not None else TreinoRepository())

    def cadastrar_treino(self, nome, series, repeticoes, id_treino):
        exercicio = ExercicioCreate(nome, series, repeticoes, id_treino)

        treino = self.treino_repository.buscar_treino_por_id(exercicio.id_treino)
        if treino is None:
            return 0

        return self.repository.inserir(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id_treino)

    def buscar_por_id(self, id_treino):
        treino = self.treino_repository.buscar_treino_por_id(id_treino)
        if treino is None:
            return None

        return self.repository.listar_por_id(id_treino)

    def atualizar(self, nome, series, repeticoes, id):
        exercicio = ExercicioUpdate(id, nome, series, repeticoes)

        resultado = self.repository.atualizar(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id)
        if resultado is None:
            return 0

        return resultado

    def deletar(self, id):
        return self.repository.deletar(id)