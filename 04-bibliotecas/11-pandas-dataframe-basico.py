# pandas
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
    "departamento": ["TI", "RH", "TI", "Financeiro", "RH"],
    "salario": [8500, 5200, 9100, 7300, 4900],
    "anos_empresa": [3, 7, 2, 5, 1],
}

df = pd.DataFrame(dados)

print(df.describe())
print()
print("Media por departamento:")
print(df.groupby("departamento")["salario"].mean().round(2))
print()
print("Acima da media salarial:")
media = df["salario"].mean()
print(df[df["salario"] > media][["nome", "salario"]])