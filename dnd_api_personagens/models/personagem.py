from models.base import db

class Personagem(db.Model):
    # Definição da Tabela
    __tablename__ = 'personagem'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    classe = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.Integer, default=1)
    
    # Campo que virá da API externa (Ex: d12 para Bárbaro)
    hit_die = db.Column(db.String(10)) 

    def __init__(self, nome, classe, nivel, hit_die):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.hit_die = hit_die
    
    def to_dict(self):
        # Auxiliar para log e debug
        return {
            "id": self.id, 
            "nome": self.nome, 
            "classe": self.classe,
            "hit_die": self.hit_die
        }