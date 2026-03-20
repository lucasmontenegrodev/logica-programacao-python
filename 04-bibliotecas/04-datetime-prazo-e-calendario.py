# datetime
from datetime import datetime

def prazo_vencido(data_str):
    prazo = datetime.strptime(data_str, "%d/%m/%Y")
    return datetime.now() > prazo

def dias_corridos_no_mes(ano, mes):
    from calendar import monthrange
    return monthrange(ano, mes)[1]

def semana_do_ano(data_str):
    dt = datetime.strptime(data_str, "%d/%m/%Y")
    return dt.isocalendar()[1]

print(prazo_vencido("01/01/2025"))
print(prazo_vencido("01/01/2027"))
print(dias_corridos_no_mes(2026, 2))
print(semana_do_ano("20/03/2026"))