# requests
import requests

def buscar_usuarios(limite=5):
    url = f"https://jsonplaceholder.typicode.com/users?_limit={limite}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def buscar_posts_do_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

usuarios = buscar_usuarios(3)
for u in usuarios:
    posts = buscar_posts_do_usuario(u["id"])
    print(f"{u['name']} — {len(posts)} posts")