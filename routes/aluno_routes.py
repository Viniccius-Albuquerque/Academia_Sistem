from fastapi import APIRouter, status, HTTPException
from schemas.aluno_schema import AlunoCreate, AlunoResponse, AlunoUpdate
from repositories.aluno_repository import AlunoRepository
from services.aluno_service import AlunoService
from typing import Literal

repository = AlunoRepository()
service = AlunoService(repository)

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoResponse, status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    result = service.cadastrar(aluno.nome, aluno.idade, aluno.plano)
    return result

@router.patch("/{id}", response_model=AlunoResponse, status_code=200)
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
    return {"mensagem": "usuario deletado com sucesso"}

@router.get("/id/{id}", response_model=AlunoResponse, status_code=200)
def buscar_aluno_id(id: int):
    result = service.buscar_por_id(id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id não encontrado")
    return result

@router.get("/", response_model=list [AlunoResponse], status_code=200)
def listar_alunos():
    result = service.listar()
    if result is []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="nao existem usuarios cadastrados")
    return result

@router.patch("/ativar/{id}", status_code=200)
def ativar_aluno(id: int):
    result = service.ativar(id)
    if result["mensagem"] == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usuario inexistente")
    if result["mensagem"] == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="usuario ja esta ativo")
    if result["mensagem"] == 1:   
        return {"mensagem": "usuario ativado com sucesso"}

@router.patch("/desativar/{id}", status_code=200)
def desativar_aluno(id: int):
    result = service.desativar(id)
    if result["mensagem"] == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usuario inexistente")
    if result["mensagem"] == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="usuario ja esta desativado")
    if result["mensagem"] == 1:   
        return {"mensagem": "usuario desativado com sucesso"}

@router.get("/plano/{plano}", response_model=list [AlunoResponse], status_code=200)
def buscar_por_plano(plano: Literal["basico", "intermediario", "pro"]):
    result = service.buscar_por_plano(plano)
    if result == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="nao existem usuarios com esse plano")
    return result
