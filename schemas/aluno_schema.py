from pydantic import BaseModel, ConfigDict, Field
from typing import Literal



class AlunoCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    idade: int = Field(gt=0)
    plano: Literal["basico", "intermediario", "pro"]
    
class AlunoUpdate(BaseModel):
    idade: int = Field(gt=0)
    plano: Literal["basico", "intermediario", "pro"]
    
class AlunoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nome: str
    idade: int
    plano: str
    estado: str
    