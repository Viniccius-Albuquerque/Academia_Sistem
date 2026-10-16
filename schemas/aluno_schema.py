from pydantic import BaseModel, ConfigDict, Field, StringConstraints
from typing import Annotated, Literal

NomeAluno = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]

class AlunoCreate(BaseModel):
    nome: NomeAluno
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