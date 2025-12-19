from dnd_api_personagens.extensions import db

class Equipamento(db.Model):
    __tablename__ = 'equipamento'
    id = db.Column(db.Integer, primary_key=True)
    personagem_id = db.Column(db.Integer, db.ForeignKey('personagem.id'), nullable=False)
    
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, default=1)
    descricao = db.Column(db.Text) # Para itens mágicos

class Arma(db.Model):
    __tablename__ = 'arma'
    id = db.Column(db.Integer, primary_key=True)
    personagem_id = db.Column(db.Integer, db.ForeignKey('personagem.id'), nullable=False)
    
    nome = db.Column(db.String(100), nullable=False)
    
    # "Ataques e magias" 
    bonus_ataque = db.Column(db.String(10)) # Ex: +5
    dano_tipo = db.Column(db.String(50))    # Ex: 1d8 Cortante
    alcance = db.Column(db.String(50))      # Ex: 5ft ou 150/600 (Ranged)
    propriedades = db.Column(db.String(200)) # Ex: Versátil, Leve

    def __init__(self, nome, dano_tipo, alcance, propriedades, personagem_id, bonus_ataque="+0"):
        self.nome = nome
        self.dano_tipo = dano_tipo
        self.alcance = alcance
        self.propriedades = propriedades
        self.personagem_id = personagem_id
        self.bonus_ataque = bonus_ataque