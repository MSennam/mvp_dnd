from dnd_api_personagens.extensions import ma
from dnd_api_personagens.models.personagem import Personagem
from dnd_api_personagens.models.magia import Magia
from dnd_api_personagens.models.equipamento import Equipamento, Arma
from marshmallow import fields


class MagiaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Magia
        include_fk = True

class EquipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Equipamento
        include_fk = True

class ArmaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Arma
        include_fk = True

class PersonagemSchema(ma.SQLAlchemyAutoSchema):
    # Campos aninhados: Traz a lista completa no JSON do personagem
    magias = fields.Nested(MagiaSchema, many=True)
    equipamentos = fields.Nested(EquipamentoSchema, many=True)
    armas = fields.Nested(ArmaSchema, many=True)

    class Meta:
        model = Personagem
        load_instance = True
        sqla_session = None