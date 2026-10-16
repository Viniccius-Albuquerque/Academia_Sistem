from pydantic import BaseModel, ConfigDict, Field

class ExercicioCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    series: int = Field(gt=0)
    repeticoes: int = Field(gt=0)
    id_treino: int = Field(gt=0)
    
class ExercicioUpdate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    series: int = Field(gt=0)
    repeticoes: int = Field(gt=0)

class ExercicioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nome: str
    series: int
    repeticoes: int
    id_treino: int