# requests
import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    data = response.json()
    return {
        "nome": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [a["ability"]["name"] for a in data["abilities"]],
    }

for nome in ["pikachu", "charizard", "bulbasaur"]:
    p = buscar_pokemon(nome)
    if p:
        print(f"{p['nome']} | tipos: {p['tipos']} | peso: {p['peso']}hg")