from datetime import datetime
from dnd_api_personagens import db

class Personagem(db.Model):
    __tablename__= "personagens" 

    #nomes em inglês devido ao fato do api externa ser em inglês 
    id = db.Column(db.Integer, primary_key=True)  # coluna ID dos personagens

    name = db.Column(db.String(80), nullable=False)  # nome obrigatório
    race = db.Column(db.String(80), nullable=False)  # raça obrigatória
    character_class = db.Column(db.String(80), nullable=False)  # classe obrigatória
    level = db.Column(db.Integer, default=1)  # nível padrão 1

    #conforme regras do jogo, o valor inicial é 10, sem contar os modificadores. 
    strength = db.Column(db.Integer, default=10)  # força padrão 10
    dexterity = db.Column(db.Integer, default=10)  # destreza padrão 10
    constitution = db.Column(db.Integer, default=10)  # constituição padrão 10
    intelligence = db.Column(db.Integer, default=10)  # inteligência padrão 10
    wisdom = db.Column(db.Integer, default=10)  # sabedoria padrão 10
    charisma = db.Column(db.Integer, default=10)  # carisma padrão 10

    max_hp = db.Column(db.Integer, default=10)  # vida máxima padrão 10
    current_hp = db.Column(db.Integer, default=10)  # vida atual padrão 10
    proficiency_bonus = db.Column(db.Integer, default=2)  # bônus proficiência padrão 2

    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # data da criação 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # data da atualização 

    def to_dict(self) -> dict:  # converte o model em dicionário (para JSON)
        return {  # começa o dict
            "id": self.id,  # id
            "name": self.name,  # nome
            "race": self.race,  # raça
            "character_class": self.character_class,  # classe
            "level": self.level,  # nível
            "strength": self.strength,  # força
            "dexterity": self.dexterity,  # destreza
            "constitution": self.constitution,  # constituição
            "intelligence": self.intelligence,  # inteligência
            "wisdom": self.wisdom,  # sabedoria
            "charisma": self.charisma,  # carisma
            "max_hp": self.max_hp,  # hp máximo
            "current_hp": self.current_hp,  # hp atual
            "proficiency_bonus": self.proficiency_bonus,  # prof bônus
            "created_at": self.created_at.isoformat() if self.created_at else None,  # timestamps em ISO
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,  # timestamps em ISO
        }  # fecha o dict