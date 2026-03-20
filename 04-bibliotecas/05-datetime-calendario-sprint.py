# datetime
from datetime import datetime, timedelta

def gerar_calendario_sprint(inicio_str, duracao_dias):
    inicio = datetime.strptime(inicio_str, "%d/%m/%Y")
    calendario = []
    for i in range(duracao_dias):
        dia = inicio + timedelta(days=i)
        tipo = "util" if dia.weekday() < 5 else "fim de semana"
        calendario.append({"data": dia.strftime("%d/%m/%Y"), "dia": dia.strftime("%A"), "tipo": tipo})
    return calendario

sprint = gerar_calendario_sprint("20/03/2026", 14)
for dia in sprint:
    print(f"{dia['data']} - {dia['dia']} - {dia['tipo']}")