from pydantic import BaseModel, ConfigDict, Field

class ExercicioCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    series: int = Field(gt=1)
    repeticoes: int = Field(gt=1)
    id_treino: int = Field(gt=0)
    
class ExercicioUpdate(BaseModel):
    id: int = Field(gt=0)
    nome: str = Field(min_length=1, max_length=100)
    series: int = Field(gt=1)
    repeticoes: int = Field(gt=1)
    
class ExercicioDelete(BaseModel):
    id: int = Field(gt=0)

class ExercicioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nome: str
    series: int
    repeticoes: int
    id_treino: int