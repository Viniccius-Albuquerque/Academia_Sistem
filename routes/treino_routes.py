from fastapi import APIRouter, status, HTTPException
from schemas.treino_schemas import (TreinoCreate, TreinoUpdate, TreinoResponse, TreinoDelete)
from repositories.treino_repository import TreinoRepository
from services.treino_service import TreinoService

repository = TreinoRepository()
service = TreinoService(repository)

router = APIRouter(prefix="/treino", tags=["Treino"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_treino(treino: TreinoCreate):
    try:
        result = service.cadastrar_treino(treino.nome, treino.dia_semana, treino.id_aluno)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    if result == -1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Dia da semana inválido")
    return result

@router.get("/{id_aluno}", response_model=list[TreinoResponse], status_code=status.HTTP_200_OK)
def listar_treino_por_id(id_aluno: int):
    result = service.buscar_por_id(id_aluno)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    return result

@router.put("/{id_aluno}", status_code=status.HTTP_200_OK)
def atualizar_treino(treino: TreinoUpdate, id_aluno: int):
    try:
        result = service.atualizar(treino.dia_semana, treino.nome, id_aluno)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    if result == -1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Dia da semana inválido")
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não possui treino nesse dia")
    return result

@router.delete("/delete", status_code=status.HTTP_200_OK)
def deletar_treino(treino: TreinoDelete):
    try:
        result = service.deletar(treino.dia_semana, treino.id_aluno)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

    if result == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno inexistente")
    if result == -2:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Dia da semana inválido")
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não possui treino nesse dia")
    return {"mensagem": "Treino excluído com sucesso"}