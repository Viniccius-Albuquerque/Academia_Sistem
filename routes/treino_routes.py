from fastapi import APIRouter, status, HTTPException
from schemas.treino_schemas import TreinoCreate, TreinoUpdate, TreinoResponse, TreinoDelete
from repositories.treino_repository import TreinoRepository
from services.treino_service import TreinoService

repository = TreinoRepository()
service = TreinoService(repository)

router = APIRouter(prefix="/treino", tags=["Treino"])

@router.post("/", status_code=201)
def criar_treino(treino: TreinoCreate):
    result = service.cadastrar_treino(treino.nome, treino.dia_semana, treino.id_aluno)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id_aluno inexistente")
    if result == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dia_semana nao existe")
    return result

@router.get("/{id_aluno}", response_model=list [TreinoResponse], status_code=200)
def listar_treino_por_id(id_aluno: int):
    result = service.buscar_por_id(id_aluno)
    if result == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="aluno nao tem treinos")
    return result

@router.put("/{id_aluno}", status_code=200)
def atualizar_treino(treino: TreinoUpdate, id_aluno: int):
    result = service.atualizar(treino.dia_semana, treino.nome, id_aluno)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id_aluno inexistente")
    if result == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dia_semana nao existe")
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="aluno tao tem treino nesse dia")
    return result

@router.delete("/delete", status_code=200)
def deletar_treino(treino: TreinoDelete):
    result = service.deletar(treino.dia_semana, treino.id_aluno)
    if result == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id_aluno inexistente")
    if result == -2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dia_semana nao existe")
    if result is 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="aluno tao tem treino nesse dia")
    return {"mensagem": "treino expurgado"}