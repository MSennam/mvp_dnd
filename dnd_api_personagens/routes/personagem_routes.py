from flask import Blueprint, request, jsonify
from services.personagem_service import PersonagemService
from schemas.personagem_schema import PersonagemSchema
import logging

# controladores com swagger

personagem_bp = Blueprint('personagem_bp', __name__)
service = PersonagemService()
schema = PersonagemSchema()
schema_lista = PersonagemSchema(many=True)
logger = logging.getLogger(__name__)

@personagem_bp.route('/personagens', methods=['GET'])
def get_personagens():
    """
    Listar todos os personagens
    ---
    responses:
      200:
        description: Lista de personagens
    """
    return jsonify(schema_lista.dump(service.listar_todos())), 200

@personagem_bp.route('/personagens', methods=['POST'])
def create_personagem():
    """
    Criar Personagem Completo
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            classe:
              type: string
            forca:
              type: integer
            destreza:
              type: integer
            pericias_proficientes:
              type: string
              example: "Athletics, Survival"
    responses:
      201:
        description: Criado com sucesso
    """
    data = request.json
    try:
        novo = service.criar_personagem(data)
        return jsonify(schema.dump(novo)), 201
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), 500

@personagem_bp.route('/personagens/<int:id>/magias', methods=['POST'])
def add_magia(id):
    """
    Adicionar Magia (Busca na API externa)
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          type: object
          properties:
            nome_magia:
              type: string
              example: "Fireball"
    """
    data = request.json
    try:
        service.adicionar_magia(id, data.get('nome_magia'))
        return jsonify(schema.dump(service.buscar_por_id(id))), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@personagem_bp.route('/personagens/<int:id>/equipamentos', methods=['POST'])
def add_equipamento(id):
    """
    Adicionar Item ao Inventário
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          type: object
          properties:
            nome:
              type: string
            quantidade:
              type: integer
    """
    try:
        service.adicionar_equipamento(id, request.json)
        return jsonify(schema.dump(service.buscar_por_id(id))), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@personagem_bp.route('/personagens/<int:id>/armas', methods=['POST'])
def add_arma(id):
    """
    Adicionar Arma (Calcula ataque automático)
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          type: object
          properties:
            nome_arma:
              type: string
              example: "Longsword"
    """
    try:
        service.adicionar_arma(id, request.json.get('nome_arma'))
        return jsonify(schema.dump(service.buscar_por_id(id))), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@personagem_bp.route('/personagens/<int:id>', methods=['DELETE'])
def delete_personagem(id):
    """
    Deletar Personagem
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    """
    if service.deletar_personagem(id):
        return jsonify({"msg": "Deletado"}), 200
    return jsonify({"erro": "Não encontrado"}), 404