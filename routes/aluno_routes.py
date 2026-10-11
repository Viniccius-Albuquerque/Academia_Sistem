from fastapi import APIRouter, status
from schemas.aluno_schema import AlunoCreate, AlunoResponse
from repositories.aluno_repository import AlunoRepository
from services.aluno_service import AlunoService

repository = AlunoRepository()
service = AlunoService(repository)

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoResponse, status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    result = service.cadastrar(aluno.nome, aluno.idade, aluno.plano)
    return result