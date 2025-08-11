from workout_api.categorias.models import CategoriaModel
from workout_api.centro_de_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Datetime, ForeignKey
from datetime import datetime

class AtletaModel(BaseModel):
    __tablename__ = 'atleta'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, primary_key=True)
    altura: Mapped[float] = mapped_column(Float, primary_key=True)
    sexo: Mapped[str] = mapped_column(String(1), primary_key=True)
    created_at = Mapped[datetime] = mapped_column(Datetime, nullable=False)
    categoria: Mapped["CategoriaModel"] = relationship("CategoriaModel", back_populates="atleta")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias", pk_id))
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship("CentroTreinamentoModel ", back_populates="atleta")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamento", pk_id))   