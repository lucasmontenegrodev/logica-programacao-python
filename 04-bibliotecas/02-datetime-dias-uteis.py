# datetime
from datetime import datetime, timedelta

def proximos_dias_uteis(n):
    hoje = datetime.now()
    uteis = []
    dia = hoje + timedelta(days=1)
    while len(uteis) < n:
        if dia.weekday() < 5:
            uteis.append(dia.strftime("%d/%m/%Y - %A"))
        dia += timedelta(days=1)
    return uteis

def diferenca_em_horas(dt1_str, dt2_str):
    fmt = "%d/%m/%Y %H:%M"
    dt1 = datetime.strptime(dt1_str, fmt)
    dt2 = datetime.strptime(dt2_str, fmt)
    diff = abs(dt2 - dt1)
    return round(diff.total_seconds() / 3600, 2)

for dia in proximos_dias_uteis(5):
    print(dia)

print(diferenca_em_horas("20/03/2026 08:00", "22/03/2026 14:30"))