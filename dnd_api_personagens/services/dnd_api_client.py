import requests
import logging

logger = logging.getLogger(__name__)

# Comunicação com a API externa
class DndApiClient:
    BASE_URL = "https://www.dnd5eapi.co/api"

    @staticmethod
    def get_class_info(class_name):
        formatted_name = class_name.lower()
        url = f"{DndApiClient.BASE_URL}/classes/{formatted_name}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            logger.error(f"Erro API Classe: {e}")
            return None

    @staticmethod
    def get_spell_info(spell_name):
        formatted_name = spell_name.lower().replace(" ", "-")
        url = f"{DndApiClient.BASE_URL}/spells/{formatted_name}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    "nome": data.get('name'),
                    "nivel": data.get('level', 0),
                    "escola": data.get('school', {}).get('name', 'Unknown'),
                    "descricao": data.get('desc', [""])[0],
                    "alcance": data.get('range'),
                    "tempo_conjuracao": data.get('casting_time')
                }
            return None
        except Exception:
            return None

    @staticmethod
    def get_weapon_info(weapon_name):
        formatted_name = weapon_name.lower().replace(" ", "-")
        url = f"{DndApiClient.BASE_URL}/equipment/{formatted_name}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('equipment_category', {}).get('index') != 'weapon':
                    return None

                damage_data = data.get('damage', {})
                dano = f"{damage_data.get('damage_dice')} {damage_data.get('damage_type', {}).get('name', '')}"
                
                props = [p.get('name') for p in data.get('properties', [])]
                
                range_info = data.get('range', {})
                alcance = f"{range_info.get('normal')}ft"
                if range_info.get('long'): alcance += f"/{range_info.get('long')}ft"

                return {
                    "nome": data.get('name'),
                    "dano_tipo": dano,
                    "alcance": alcance,
                    "propriedades": ", ".join(props)
                }
            return None
        except Exception:
            return None