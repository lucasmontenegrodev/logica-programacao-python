# requests
import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return data
    return None

cep = buscar_cep("50000000")
if cep:
    print(f"{cep['logradouro']}, {cep['bairro']}, {cep['localidade']} - {cep['uf']}")