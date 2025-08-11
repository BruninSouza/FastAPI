from workout_api.contrib.schemas import BaseSchema

from pydantic import Field, PositiveFloat
from typing import Annotated

class Atleta(BaseSchema):
    nome: str = Annotated(str, Field(description="Nome do atleta", examples="João Silva", max_length=50))
    cpf: str = Annotated(str, Field(description="CPF do atleta", examples="12345678900", max_length=11))
    idade: str = Annotated(int, Field(description="Idade do atleta", examples=25))
    peso: str = Annotated(PositiveFloat, Field(description="Peso do atleta", examples=87.5))
    altura: str = Annotated(PositiveFloat, Field(description="Altura do atleta", examples=1.70))
    sexo: str = Annotated(str, Field(description="Sexo do atleta", examples="M", max_length=1))
