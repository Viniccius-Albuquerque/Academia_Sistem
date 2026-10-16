from fastapi import APIRouter, status, HTTPException
from schemas.aluno_schema import AlunoCreate, AlunoResponse, AlunoUpdate
from repositories.aluno_repository import AlunoRepository
from services.aluno_service import AlunoService
from typing import Literal

repository = AlunoRepository()
service = AlunoService(repository)

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_aluno(aluno: AlunoCreate):
    try:
        return service.cadastrar(aluno.nome, aluno.idade, aluno.plano)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

@router.patch("/{id}", response_model=AlunoResponse)
def atualizar_aluno(id: int, naluno: AlunoUpdate):
    try:
        result = service.atualizar(id, naluno.idade, naluno.plano)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID não encontrado")
    return result

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deletar_aluno(id: int):
    result = service.deletar(id)

    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID não encontrado")
    return {"mensagem": "Aluno deletado com sucesso"}

@router.get("/id/{id}", response_model=AlunoResponse)
def buscar_aluno_id(id: int):
    result = service.buscar_por_id(id)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID não encontrado")
    return result

@router.get("/", response_model=list[AlunoResponse])
def listar_alunos():
    return service.listar()

@router.patch("/ativar/{id}")
def ativar_aluno(id: int):
    result = service.ativar(id)

    if result["mensagem"] == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    if result["mensagem"] == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Aluno já está ativo")
    return {"mensagem": "Aluno ativado com sucesso"}

@router.patch("/desativar/{id}")
def desativar_aluno(id: int):
    result = service.desativar(id)

    if result["mensagem"] == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    if result["mensagem"] == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Aluno já está desativado")
    return {"mensagem": "Aluno desativado com sucesso"}

@router.get("/plano/{plano}", response_model=list[AlunoResponse])
def buscar_por_plano(plano: Literal["basico", "intermediario", "pro"]):
    result = service.buscar_por_plano(plano)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existem alunos com esse plano")
    return result