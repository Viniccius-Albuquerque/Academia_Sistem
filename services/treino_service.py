
from modules.treino import TreinoCreate, TreinoUpdate, TreinoDelete
from repositories.aluno_repository import AlunoRepository
from repositories.exercicio_repository import ExercicioRepository
from services.exercicio_service import ExercicioService

class TreinoService:

    def __init__(self, repository, aluno_repository=None, exercicio_service=None):
        self.repository = repository
        self.aluno_repository = (aluno_repository if aluno_repository is not None else AlunoRepository())
        self.exercicio_service = (exercicio_service if exercicio_service is not None else ExercicioService(ExercicioRepository()))

    def cadastrar_treino(self, nome, dia_semana, id_aluno):
        treino = TreinoCreate(nome, dia_semana, id_aluno)

        aluno = self.aluno_repository.buscar_por_id(treino.id_aluno)
        if aluno is None:
            return 0

        dias_validos = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

        if treino.dia_semana not in dias_validos:
            return -1

        return self.repository.inserir(treino.nome, treino.dia_semana, treino.id_aluno)

    def buscar_por_id(self, id_aluno):
        aluno = self.aluno_repository.buscar_por_id(id_aluno)
        if aluno is None:
            return None

        return self.repository.listar_por_id(id_aluno)

    def atualizar(self, dia_semana, nome, id_aluno):
        treino = TreinoUpdate(nome, dia_semana, id_aluno)

        aluno = self.aluno_repository.buscar_por_id(treino.id_aluno)
        if aluno is None:
            return 0

        dias_validos = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

        if treino.dia_semana not in dias_validos:
            return -1

        return self.repository.atualizar(treino.dia_semana, treino.nome, treino.id_aluno)

    def deletar(self, dia_semana, id_aluno):
        treino = TreinoDelete(dia_semana, id_aluno)
        dias_validos = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

        if treino.dia_semana not in dias_validos:
            return -2

        aluno = self.aluno_repository.buscar_por_id(treino.id_aluno)
        if aluno is None:
            return -1

        treinos = self.repository.listar_por_id(treino.id_aluno)
        treinos_do_dia = [item for item in treinos if item["dia_semana"] == treino.dia_semana]

        if not treinos_do_dia:
            return 0

        for item in treinos_do_dia:
            exercicios = self.exercicio_service.buscar_por_id(item["id"])
            if exercicios:
                for exercicio in exercicios:
                    self.exercicio_service.deletar(exercicio["id"])

        return self.repository.deletar(treino.dia_semana, treino.id_aluno)