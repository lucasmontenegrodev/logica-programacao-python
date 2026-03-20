# pandas
import pandas as pd

vendas = pd.DataFrame({
    "data": ["2026-01-05","2026-01-12","2026-02-03","2026-02-18","2026-03-07","2026-03-20"],
    "produto": ["Notebook","Mouse","Notebook","Teclado","Mouse","Notebook"],
    "quantidade": [2, 5, 1, 3, 8, 2],
    "preco_unitario": [3500, 120, 3500, 280, 120, 3500],
})

vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]
vendas["mes"] = pd.to_datetime(vendas["data"]).dt.to_period("M")

print("Total por produto:")
print(vendas.groupby("produto")["total"].sum())
print()
print("Total por mes:")
print(vendas.groupby("mes")["total"].sum())
print()
print("Produto mais vendido (quantidade):")
print(vendas.groupby("produto")["quantidade"].sum().idxmax())