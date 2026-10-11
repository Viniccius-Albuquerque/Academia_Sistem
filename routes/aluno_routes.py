from fastapi import APIRouter, status, HTTPException
from schemas.aluno_schema import AlunoCreate, AlunoResponse, AlunoUpdate
from repositories.aluno_repository import AlunoRepository
from services.aluno_service import AlunoService

repository = AlunoRepository()
service = AlunoService(repository)

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoResponse, status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    result = service.cadastrar(aluno.nome, aluno.idade, aluno.plano)
    return result

@router.put("/{id}", response_model=AlunoResponse, status_code=200)
def atualizar_aluno(id: int, naluno:AlunoUpdate):
    result = service.atualizar(id, naluno.idade, naluno.plano)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id não encontrado")
    return result

@router.delete("/{id}", status_code=200)
def deletar_aluno(id: int):
    result = service.deletar(id)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id não encontrado")
    return {"mensage": "usuario deletado com sucesso"}

@router.get("/{id}", response_model=AlunoResponse, status_code=200)
def buscar_aluno_id(id: int):
    result = service.buscar_por_id(id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id não encontrado")
    return result

@router.get("/", response_model=list [AlunoResponse], status_code=200)
def listar_alunos():
    result = service.listar()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="nao existem usuarios cadastrados")
    return result