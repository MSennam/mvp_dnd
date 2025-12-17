from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from models.base import db
from routes.personagem_routes import personagem_bp

def create_app():
    app = Flask(__name__)
    CORS(app) 

    # Configuração do Banco de Dados 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dnd_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização do Banco
    db.init_app(app)

    # Configuração do Swagger 
    app.config['SWAGGER'] = {
        'title': 'D&D Personagens API',
        'uiversion': 3
    }
    Swagger(app)

    # Registro das Rotas (Blueprints)
    app.register_blueprint(personagem_bp)

    # Criação das tabelas no banco ao iniciar
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    # Debug=True ajuda no desenvolvimento, mas deve ser False em produção
    app.run(debug=True, host='0.0.0.0', port=5000)