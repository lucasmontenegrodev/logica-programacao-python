# requests
import requests

def verificar_status_api(url):
    try:
        response = requests.get(url, timeout=5)
        return {"url": url, "status": response.status_code, "ok": response.ok}
    except requests.exceptions.Timeout:
        return {"url": url, "status": "timeout", "ok": False}
    except requests.exceptions.ConnectionError:
        return {"url": url, "status": "connection_error", "ok": False}

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/99999",
    "https://viacep.com.br/ws/01001000/json/",
]

for url in urls:
    resultado = verificar_status_api(url)
    print(f"{resultado['status']} | {'OK' if resultado['ok'] else 'FALHOU'} | {url}")