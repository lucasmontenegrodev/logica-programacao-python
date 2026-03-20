# pandas
import pandas as pd

bugs = pd.DataFrame({
    "id": ["BUG-001","BUG-002","BUG-003","BUG-004","BUG-005","BUG-006","BUG-007","BUG-008"],
    "severidade": ["Critica","Alta","Media","Critica","Baixa","Alta","Media","Alta"],
    "status": ["Aberto","Fechado","Aberto","Fechado","Aberto","Aberto","Fechado","Aberto"],
    "sprint": [1, 1, 2, 1, 2, 3, 2, 3],
    "dias_aberto": [5, 3, 12, 2, 20, 8, 7, 4],
})

print("Bugs por severidade:")
print(bugs["severidade"].value_counts())
print()
print("Bugs abertos por sprint:")
abertos = bugs[bugs["status"] == "Aberto"]
print(abertos.groupby("sprint").size())
print()
print("Media de dias aberto por severidade:")
print(bugs.groupby("severidade")["dias_aberto"].mean().round(1))
print()
print("Taxa de resolucao por sprint (%):")
total = bugs.groupby("sprint").size()
fechados = bugs[bugs["status"] == "Fechado"].groupby("sprint").size()
taxa = (fechados / total * 100).fillna(0).round(1)
print(taxa)