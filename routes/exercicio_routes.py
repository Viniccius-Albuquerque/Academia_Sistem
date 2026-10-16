from fastapi import APIRouter, status, HTTPException
from schemas.exercicio_schema import ExercicioCreate, ExercicioResponse, ExercicioUpdate
from repositories.exercicio_repository import ExercicioRepository
from services.exercicio_service import ExercicioService

repository = ExercicioRepository()
service = ExercicioService(repository)

router = APIRouter(prefix="/exercicio", tags=["Exercicio"])

@router.post("/", response_model=ExercicioResponse, status_code=201)
def criar_exercicio(exercicio: ExercicioCreate):
    result = service.cadastrar_treino(exercicio.nome, exercicio.series, exercicio.repeticoes, exercicio.id_treino)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id nao encontrado")
    return result

@router.get("/{id_treino}", response_model=list [ExercicioResponse], status_code=200)
def listar_exercicios(id_treino: int):
    result = service.buscar_por_id(id_treino)
    if result == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="treino nao tem exercicios")
    return result

@router.put("/atualizar/{id}", response_model=ExercicioResponse, status_code=200)
def atualizar_exercicio(exercicio: ExercicioUpdate, id: int):
    result = service.atualizar(exercicio.nome, exercicio.series, exercicio.repeticoes, id)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id nao encontrado")
    return result

@router.delete("/delete/{id}", status_code=200)
def deletar_exercicio(id: int):
    result = service.deletar(id)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id nao encontrado")
    return {"mensagem": "exercicio expurgado"}