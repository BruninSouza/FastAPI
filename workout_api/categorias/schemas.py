from pydantic import Field
from typing_extensions import Annotated
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: str = Annotated(str, Field(description="Nome da categoria", examples="Scale", max_length=10))