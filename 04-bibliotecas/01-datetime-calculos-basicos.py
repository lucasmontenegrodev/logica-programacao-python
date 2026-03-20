# datetime
from datetime import datetime, timedelta

def dias_ate_ano_novo():
    hoje = datetime.now()
    ano_novo = datetime(hoje.year + 1, 1, 1)
    return (ano_novo - hoje).days

def idade_em_dias(data_nascimento_str):
    nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    return (datetime.now() - nascimento).days

def eh_fim_de_semana(data_str):
    data = datetime.strptime(data_str, "%d/%m/%Y")
    return data.weekday() >= 5

print(dias_ate_ano_novo())
print(idade_em_dias("15/03/1995"))
print(eh_fim_de_semana("22/03/2026"))
print(eh_fim_de_semana("20/03/2026"))