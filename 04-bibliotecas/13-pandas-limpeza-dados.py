# pandas
import pandas as pd
import io

csv_data = """id,nome,email,idade,cidade
1,Ana Silva,ana@email.com,28,Recife
2,Bruno Costa,,35,Sao Paulo
3,Carlos Lima,carlos@email.com,,Rio de Janeiro
4,Diana Souza,diana@email.com,29,
5,,erro@email.com,31,Belo Horizonte"""

df = pd.read_csv(io.StringIO(csv_data))

print("Valores nulos por coluna:")
print(df.isnull().sum())

df["nome"].fillna("Desconhecido", inplace=True)
df["cidade"].fillna("Nao informada", inplace=True)
df.dropna(subset=["email"], inplace=True)
df["idade"] = df["idade"].fillna(df["idade"].median())

print()
print("Apos limpeza:")
print(df)