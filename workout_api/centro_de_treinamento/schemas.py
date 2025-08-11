from pydantic import Field
from typing_extensions import Annotated
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: str = Annotated(str, Field(description="Nome do centro de treinamento", examples="CT Mambo", max_length=20))
    endereco: str = Annotated(str, Field(description="Endereço do centro de treinamento", examples="Rua x, Quadra 05", max_length=60))
    proprietario: str = Annotated(str, Field(description="Proprietario do centro de treinamento", examples="Manoel Mamam Silva", max_length=30))