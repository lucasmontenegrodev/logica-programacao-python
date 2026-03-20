import os

EX01 = """# datetime
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
"""

EX02 = """# datetime
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
"""

EX03 = """# datetime
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
"""

EX04 = """# datetime
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
"""

EX05 = """# datetime
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
"""

EX06 = """# requests
import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return data
    return None

cep = buscar_cep("50000000")
if cep:
    print(f"{cep['logradouro']}, {cep['bairro']}, {cep['localidade']} - {cep['uf']}")
"""

EX07 = """# requests
import requests

def buscar_usuarios(limite=5):
    url = f"https://jsonplaceholder.typicode.com/users?_limit={limite}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def buscar_posts_do_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

usuarios = buscar_usuarios(3)
for u in usuarios:
    posts = buscar_posts_do_usuario(u["id"])
    print(f"{u['name']} — {len(posts)} posts")
"""

EX08 = """# requests
import requests

def criar_post(titulo, corpo, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": titulo, "body": corpo, "userId": user_id}
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json(), response.status_code

def deletar_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url, timeout=10)
    return response.status_code

post, status = criar_post("Meu titulo", "Conteudo do post", 1)
print(f"Post criado — ID: {post['id']} | Status: {status}")

status_delete = deletar_post(1)
print(f"Post deletado — Status: {status_delete}")
"""

EX09 = """# requests
import requests

def verificar_status_api(url):
    try:
        response = requests.get(url, timeout=5)
        return {"url": url, "status": response.status_code, "ok": response.ok}
    except requests.exceptions.Timeout:
        return {"url": url, "status": "timeout", "ok": False}
    except requests.exceptions.ConnectionError:
        return {"url": url, "status": "connection_error", "ok": False}

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/99999",
    "https://viacep.com.br/ws/01001000/json/",
]

for url in urls:
    resultado = verificar_status_api(url)
    print(f"{resultado['status']} | {'OK' if resultado['ok'] else 'FALHOU'} | {url}")
"""

EX10 = """# requests
import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    data = response.json()
    return {
        "nome": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [a["ability"]["name"] for a in data["abilities"]],
    }

for nome in ["pikachu", "charizard", "bulbasaur"]:
    p = buscar_pokemon(nome)
    if p:
        print(f"{p['nome']} | tipos: {p['tipos']} | peso: {p['peso']}hg")
"""

EX11 = """# pandas
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
"""

EX12 = """# pandas
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
"""

EX13 = """# pandas
import pandas as pd
import io

csv_data = \"\"\"id,nome,email,idade,cidade
1,Ana Silva,ana@email.com,28,Recife
2,Bruno Costa,,35,Sao Paulo
3,Carlos Lima,carlos@email.com,,Rio de Janeiro
4,Diana Souza,diana@email.com,29,
5,,erro@email.com,31,Belo Horizonte\"\"\"

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
"""

EX14 = """# pandas
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
"""

EX15 = """# pandas + requests
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
"""

arquivos = {
    "04-bibliotecas/01-datetime-calculos-basicos.py":       EX01,
    "04-bibliotecas/02-datetime-dias-uteis.py":             EX02,
    "04-bibliotecas/03-datetime-agrupamento-por-mes.py":    EX03,
    "04-bibliotecas/04-datetime-prazo-e-calendario.py":     EX04,
    "04-bibliotecas/05-datetime-calendario-sprint.py":      EX05,
    "04-bibliotecas/06-requests-viacep.py":                 EX06,
    "04-bibliotecas/07-requests-jsonplaceholder-get.py":    EX07,
    "04-bibliotecas/08-requests-post-delete.py":            EX08,
    "04-bibliotecas/09-requests-verificador-status.py":     EX09,
    "04-bibliotecas/10-requests-pokeapi.py":                EX10,
    "04-bibliotecas/11-pandas-dataframe-basico.py":         EX11,
    "04-bibliotecas/12-pandas-vendas-agrupamento.py":       EX12,
    "04-bibliotecas/13-pandas-limpeza-dados.py":            EX13,
    "04-bibliotecas/14-pandas-analise-bugs.py":             EX14,
    "04-bibliotecas/15-pandas-requests-integracao.py":      EX15,
}

print("Adicionando exercicios ao logica-programacao-python...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print(f"\nPronto. {len(arquivos)} arquivos criados.")
print("\nProximos passos:")
print("  git add .")
print('  git commit -m "feat: adiciona 15 exercicios de bibliotecas Python"')
print("  git push")
