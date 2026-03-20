# pandas + requests
import pandas as pd
import requests

def buscar_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
    response.raise_for_status()
    return response.json()

posts = buscar_posts()
df = pd.DataFrame(posts)

print(f"Total de posts: {len(df)}")
print()
print("Posts por usuario:")
print(df.groupby("userId").size().rename("total_posts"))
print()
df["tamanho_titulo"] = df["title"].str.len()
df["tamanho_corpo"] = df["body"].str.len()
print("Media de caracteres no titulo:", df["tamanho_titulo"].mean().round(1))
print("Media de caracteres no corpo:", df["tamanho_corpo"].mean().round(1))
print()
print("Usuario com mais posts:")
print(df.groupby("userId").size().idxmax())