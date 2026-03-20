# datetime
from datetime import datetime

def agrupar_por_mes(datas):
    grupos = {}
    for d in datas:
        dt = datetime.strptime(d, "%d/%m/%Y")
        chave = dt.strftime("%Y-%m")
        grupos.setdefault(chave, []).append(d)
    return grupos

def formatar_data_extenso(data_str):
    meses = ["janeiro","fevereiro","marco","abril","maio","junho",
             "julho","agosto","setembro","outubro","novembro","dezembro"]
    dt = datetime.strptime(data_str, "%d/%m/%Y")
    return f"{dt.day} de {meses[dt.month - 1]} de {dt.year}"

datas = ["05/01/2026","12/01/2026","03/02/2026","20/03/2026","25/03/2026"]
for mes, lista in agrupar_por_mes(datas).items():
    print(f"{mes}: {lista}")

print(formatar_data_extenso("20/03/2026"))