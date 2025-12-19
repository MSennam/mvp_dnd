from dnd_api_personagens.extensions import db

#classe para gerenciar as magias dos personagens
class Magia(db.Model):
    __tablename__ = 'magia'

    id = db.Column(db.Integer, primary_key=True)
    personagem_id = db.Column(db.Integer, db.ForeignKey('personagem.id'), nullable=False)
    
    nome = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.Integer, default=0)
    escola = db.Column(db.String(50))
    tempo_conjuracao = db.Column(db.String(50))
    alcance = db.Column(db.String(50))
    descricao = db.Column(db.Text)

    def __init__(self, nome, nivel, escola, descricao, personagem_id):
        self.nome = nome
        self.nivel = nivel
        self.escola = escola
        self.descricao = descricao
        self.personagem_id = personagem_id
