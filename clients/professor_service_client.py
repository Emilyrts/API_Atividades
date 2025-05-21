import requests

PROFESSOR_SERVICE_URL = "http://localhost:5000/professores"


class professorServiceClient:
    @staticmethod
    def verificar_professor(id_professor):
        url = f"{PROFESSOR_SERVICE_URL}/professores/{id_professor}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('professores', False) if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o professor_service: {e}")
            return False
