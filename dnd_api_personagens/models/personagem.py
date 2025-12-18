from models.base import db
from sqlalchemy.orm import relationship

class Personagem(db.Model):
    __tablename__ = 'personagem'

    # --- Cabeçalho (Página 1) ---
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    jogador_nome = db.Column(db.String(100))
    classe = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.Integer, default=1)
    raca = db.Column(db.String(50))
    antecedente = db.Column(db.String(50))
    alinhamento = db.Column(db.String(50))
    xp = db.Column(db.Integer, default=0)

    # --- Atributos Principais ---
    forca = db.Column(db.Integer, default=10)
    destreza = db.Column(db.Integer, default=10)
    constituicao = db.Column(db.Integer, default=10)
    inteligencia = db.Column(db.Integer, default=10)
    sabedoria = db.Column(db.Integer, default=10)
    carisma = db.Column(db.Integer, default=10)

    # --- Combate e Vida ---
    classe_armadura = db.Column(db.Integer, default=10)
    iniciativa = db.Column(db.Integer, default=0)
    deslocamento = db.Column(db.Integer, default=30)
    hp_maximo = db.Column(db.Integer, default=10)
    hp_atual = db.Column(db.Integer, default=10)
    hit_die = db.Column(db.String(10))

    # --- Perícias e Saves ---
    pericias_proficientes = db.Column(db.Text, default="")
    saves_proficientes = db.Column(db.Text, default="") 

    # --- Roleplay ---
    tracos_personalidade = db.Column(db.Text)
    ideais = db.Column(db.Text)
    vinculos = db.Column(db.Text)
    fraquezas = db.Column(db.Text)

    # --- Relacionamentos ---
    magias = relationship('Magia', backref='personagem', lazy=True, cascade="all, delete-orphan")
    equipamentos = relationship('Equipamento', backref='personagem', lazy=True, cascade="all, delete-orphan")
    armas = relationship('Arma', backref='personagem', lazy=True, cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super(Personagem, self).__init__(**kwargs)
        if self.hp_atual is None:
            self.hp_atual = self.hp_maximo
