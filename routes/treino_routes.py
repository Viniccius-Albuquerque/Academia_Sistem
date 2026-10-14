from fastapi import APIRouter, status, HTTPException
from schemas.treino_schemas import TreinoCreate, TreinoUpdate, TreinoResponse
from repositories.treino_repository import TreinoRepository
from services.treino_service import TreinoService

repository = TreinoRepository()
service = TreinoService(repository)

router = APIRouter(prefix="/treino", tags=["Treino"])

@router.post("/", response_model=TreinoResponse, status_code=201)
def criar_treino(treino: TreinoCreate):
    result = service.cadastrar_treino(treino.nome, treino.dia_semana, treino.id_aluno)
    return result

@router.get("/{id_aluno}", response_model=list [TreinoResponse], status_code=200)
def listar_treino_por_id(id_aluno: int):
    result = service.buscar_por_id(id_aluno)
    return result

@router.put("/{id_aluno}", response_model=TreinoResponse, status_code=200)
def atualizar_treino(treino: TreinoUpdate, id_aluno: int):
    result = service.atualizar(treino.dia_semana, treino.nome, id_aluno)
    return result