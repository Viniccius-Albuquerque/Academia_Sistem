from pydantic import BaseModel, ConfigDict, Field

class TreinoCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    dia_semana: str = Field(min_length=1, max_length=100)
    id_aluno: int = Field(gt=0)
    
class TreinoUpdate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    dia_semana: str = Field(min_length=1, max_length=100)
    
class TreinoDelete(BaseModel):
    dia_semana: str = Field(min_length=1, max_length=100)
    id_aluno: int = Field(gt=0)

class TreinoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nome: str
    dia_semana: str
    id_aluno: int