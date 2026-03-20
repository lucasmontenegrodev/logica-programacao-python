# requests
import requests

def criar_post(titulo, corpo, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": titulo, "body": corpo, "userId": user_id}
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json(), response.status_code

def deletar_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url, timeout=10)
    return response.status_code

post, status = criar_post("Meu titulo", "Conteudo do post", 1)
print(f"Post criado — ID: {post['id']} | Status: {status}")

status_delete = deletar_post(1)
print(f"Post deletado — Status: {status_delete}")