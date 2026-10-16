from fastapi import APIRouter, status, HTTPException
from schemas.exercicio_schema import (ExercicioCreate, ExercicioResponse, ExercicioUpdate)
from repositories.exercicio_repository import ExercicioRepository
from services.exercicio_service import ExercicioService

repository = ExercicioRepository()
service = ExercicioService(repository)

router = APIRouter(prefix="/exercicio", tags=["Exercicio"])

@router.post("/", response_model=ExercicioResponse, status_code=status.HTTP_201_CREATED)
def criar_exercicio(exercicio: ExercicioCreate):
    try:
        result = service.cadastrar_treino(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id_treino)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Treino inexistente")
    return result

@router.get("/{id_treino}", response_model=list[ExercicioResponse], status_code=status.HTTP_200_OK)
def listar_exercicios(id_treino: int):
    result = service.buscar_por_id(id_treino)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Treino inexistente")
    return result

@router.put("/atualizar/{id}", response_model=ExercicioResponse, status_code=status.HTTP_200_OK)
def atualizar_exercicio(exercicio: ExercicioUpdate, id: int):
    try:
        result = service.atualizar(exercicio.nome, exercicio.series, exercicio.repeticoes, id)
    except ValueError as erro:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(erro))

    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercício inexistente")
    return result

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
def deletar_exercicio(id: int):
    result = service.deletar(id)

    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercício inexistente")
    return {"mensagem": "Exercício excluído com sucesso"}
