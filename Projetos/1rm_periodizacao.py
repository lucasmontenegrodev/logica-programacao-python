"""
Sistema de Periodização e 1RM
Versão avançada com menu, histórico, múltiplas fórmulas e exportação.
"""

import json
import os
from datetime import datetime

ARQUIVO_DADOS = "meus_treinos.json"

# ─────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def input_float(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if valor > 0:
                return valor
            print("  ⚠ Digite um número positivo.")
        except ValueError:
            print("  ⚠ Entrada inválida. Digite um número.")


def input_int(mensagem: str, minimo: int = 1) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor >= minimo:
                return valor
            print(f"  ⚠ Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("  ⚠ Entrada inválida. Digite um número inteiro.")


def input_sim_nao(mensagem: str) -> bool:
    while True:
        r = input(mensagem).strip().lower()
        if r in ("sim", "s"):
            return True
        if r in ("não", "nao", "n"):
            return False
        print("  ⚠ Responda com sim ou não.")


# ─────────────────────────────────────────────
# PERSISTÊNCIA (JSON)
# ─────────────────────────────────────────────

def carregar_dados() -> dict:
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"perfil": {}, "historico": []}


def salvar_dados(dados: dict):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"  ✅ Dados salvos em '{ARQUIVO_DADOS}'")


# ─────────────────────────────────────────────
# CÁLCULO DE 1RM  (múltiplas fórmulas)
# ─────────────────────────────────────────────

FORMULAS_1RM = {
    "1": ("Epley",       lambda p, r: p * (1 + r / 30)),
    "2": ("Brzycki",     lambda p, r: p * (36 / (37 - r))),
    "3": ("Lombardi",    lambda p, r: p * (r ** 0.10)),
    "4": ("O'Conner",    lambda p, r: p * (1 + 0.025 * r)),
}


def calcular_1rm_por_formula() -> float:
    print("\n📐 Calcular 1RM a partir de uma série")
    peso = input_float("  Peso utilizado na série (Kg): ")
    reps = input_int("  Repetições realizadas: ", minimo=1)

    if reps == 1:
        print("  ℹ Com 1 repetição, o peso já é o seu 1RM.")
        return peso

    print("\n  Escolha a fórmula:")
    for k, (nome, _) in FORMULAS_1RM.items():
        print(f"  [{k}] {nome}")

    escolha = input("  Opção: ").strip()
    if escolha not in FORMULAS_1RM:
        print("  ⚠ Opção inválida. Usando Epley.")
        escolha = "1"

    nome, formula = FORMULAS_1RM[escolha]
    resultado = formula(peso, reps)
    print(f"\n  🏋 1RM estimado ({nome}): {resultado:.2f} Kg")
    return round(resultado, 2)


# ─────────────────────────────────────────────
# PERIODIZAÇÃO
# ─────────────────────────────────────────────

MODELOS_PERIODIZACAO = {
    "1": "Linear (iniciante / intermediário)",
    "2": "Ondulatória Semanal (intermediário / avançado)",
    "3": "Bloco (avançado)",
}

def gerar_periodizacao(um_rm: float, modelo: str) -> list[dict]:
    semanas = []

    if modelo == "1":  # Linear
        plano = [
            (1, 0.60, "12–15", "Adaptação"),
            (2, 0.70, "10–12", "Volume"),
            (3, 0.80, "8–10",  "Hipertrofia"),
            (4, 0.90, "6–8",   "Força"),
            (5, 1.00, "1–3",   "Teste de 1RM"),
            (6, 0.50, "15–20", "Recuperação ativa"),
        ]
    elif modelo == "2":  # Ondulatória
        plano = [
            (1, 0.70, "10–12", "Volume alto"),
            (2, 0.80, "8–10",  "Hipertrofia"),
            (3, 0.85, "6–8",   "Força-hipertrofia"),
            (4, 0.90, "4–6",   "Força máxima"),
            (5, 0.95, "2–4",   "Pico de força"),
            (6, 0.55, "12–15", "Deload"),
        ]
    else:  # Bloco
        plano = [
            (1, 0.65, "15–20", "Bloco acumulação – volume"),
            (2, 0.70, "12–15", "Bloco acumulação – volume"),
            (3, 0.80, "8–10",  "Bloco transmutação – força"),
            (4, 0.85, "6–8",   "Bloco transmutação – força"),
            (5, 0.92, "3–5",   "Bloco realização – pico"),
            (6, 0.50, "10–15", "Deload"),
        ]

    for semana, pct, reps, descricao in plano:
        semanas.append({
            "semana": semana,
            "percentual": int(pct * 100),
            "carga_kg": round(um_rm * pct, 2),
            "repeticoes": reps,
            "descricao": descricao,
        })
    return semanas


def exibir_periodizacao(exercicio: str, um_rm: float, semanas: list[dict]):
    print(f"\n  📋 Periodização — {exercicio}  (1RM: {um_rm} Kg)")
    print("  " + "─" * 60)
    print(f"  {'Sem':>3}  {'%':>4}  {'Carga (Kg)':>10}  {'Reps':>7}  Descrição")
    print("  " + "─" * 60)
    for s in semanas:
        print(
            f"  {s['semana']:>3}  {s['percentual']:>3}%"
            f"  {s['carga_kg']:>10.2f}  {s['repeticoes']:>7}  {s['descricao']}"
        )
    print("  " + "─" * 60)


# ─────────────────────────────────────────────
# FLUXO PRINCIPAL
# ─────────────────────────────────────────────

def configurar_treino(dados: dict):
    limpar_tela()
    print("═" * 55)
    print("  🏋  CONFIGURAR NOVO PLANO DE TREINO")
    print("═" * 55)

    # Dias de treino
    DIAS = ["segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"]
    meus_dias = [d for d in DIAS if input_sim_nao(f"  Treina na {d}? (sim/não): ")]
    if not meus_dias:
        print("  ⚠ Nenhum dia selecionado. Voltando ao menu.")
        return

    print(f"\n  📅 Seus dias: {', '.join(meus_dias)}")

    # Modelo de periodização
    print("\n  Escolha o modelo de periodização:")
    for k, v in MODELOS_PERIODIZACAO.items():
        print(f"  [{k}] {v}")
    modelo = input("  Opção: ").strip()
    if modelo not in MODELOS_PERIODIZACAO:
        modelo = "1"

    print(f"\n  ✅ Modelo: {MODELOS_PERIODIZACAO[modelo]}\n")

    # Exercícios por dia
    registro = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "modelo": MODELOS_PERIODIZACAO[modelo],
        "dias": {},
    }

    for dia in meus_dias:
        print(f"\n  ── {dia.upper()} ──")
        qnt = input_int(f"  Quantos exercícios em {dia}? ")
        registro["dias"][dia] = []

        for i in range(qnt):
            print(f"\n  Exercício {i + 1}:")
            exercicio = input("    Nome do exercício: ").strip().title()

            # Entrada do 1RM
            print("    Como informar o 1RM?")
            print("    [1] Informar diretamente")
            print("    [2] Calcular a partir de uma série")
            opcao_rm = input("    Opção: ").strip()

            if opcao_rm == "2":
                um_rm = calcular_1rm_por_formula()
            else:
                um_rm = input_float(f"    1RM de {exercicio} (Kg): ")

            semanas = gerar_periodizacao(um_rm, modelo)
            exibir_periodizacao(exercicio, um_rm, semanas)

            registro["dias"][dia].append({
                "exercicio": exercicio,
                "um_rm": um_rm,
                "periodizacao": semanas,
            })

    dados["historico"].append(registro)
    salvar_dados(dados)
    print("\n  ✅ Plano salvo com sucesso!")
    input("\n  Pressione Enter para continuar...")


def ver_historico(dados: dict):
    limpar_tela()
    historico = dados.get("historico", [])
    if not historico:
        print("  ℹ Nenhum plano salvo ainda.")
        input("\n  Pressione Enter para continuar...")
        return

    print("═" * 55)
    print("  📂  HISTÓRICO DE PLANOS")
    print("═" * 55)

    for idx, plano in enumerate(historico, 1):
        print(f"\n  [{idx}] {plano['data']}  —  {plano['modelo']}")
        for dia, exercicios in plano["dias"].items():
            nomes = ", ".join(e["exercicio"] for e in exercicios)
            print(f"       {dia}: {nomes}")

    print()
    ver = input_int("  Ver detalhes de qual plano? (0 = voltar): ", minimo=0)
    if ver == 0 or ver > len(historico):
        return

    plano = historico[ver - 1]
    print(f"\n  Plano de {plano['data']}  —  {plano['modelo']}")
    for dia, exercicios in plano["dias"].items():
        for ex in exercicios:
            exibir_periodizacao(ex["exercicio"], ex["um_rm"], ex["periodizacao"])

    input("\n  Pressione Enter para continuar...")


def exportar_txt(dados: dict):
    historico = dados.get("historico", [])
    if not historico:
        print("  ℹ Nenhum plano para exportar.")
        input("\n  Pressione Enter para continuar...")
        return

    nome_arquivo = f"plano_treino_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    linhas = []

    for plano in historico:
        linhas.append(f"{'═' * 55}")
        linhas.append(f"  Plano: {plano['data']}  |  Modelo: {plano['modelo']}")
        linhas.append(f"{'═' * 55}")
        for dia, exercicios in plano["dias"].items():
            linhas.append(f"\n  {dia.upper()}")
            for ex in exercicios:
                linhas.append(f"\n  {ex['exercicio']}  (1RM: {ex['um_rm']} Kg)")
                linhas.append(f"  {'Sem':>3}  {'%':>4}  {'Carga':>8}  {'Reps':>7}  Fase")
                for s in ex["periodizacao"]:
                    linhas.append(
                        f"  {s['semana']:>3}  {s['percentual']:>3}%"
                        f"  {s['carga_kg']:>7.2f}Kg  {s['repeticoes']:>7}  {s['descricao']}"
                    )
        linhas.append("")

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"\n  ✅ Exportado para '{nome_arquivo}'")
    input("\n  Pressione Enter para continuar...")


def calcular_1rm_avulso():
    limpar_tela()
    print("═" * 55)
    print("  📐  CALCULADORA DE 1RM")
    print("═" * 55)
    calcular_1rm_por_formula()
    input("\n  Pressione Enter para continuar...")


def menu_principal():
    dados = carregar_dados()

    while True:
        limpar_tela()
        print("═" * 55)
        print("  🏋  SISTEMA DE PERIODIZAÇÃO E 1RM")
        print("═" * 55)
        print("  [1] Configurar novo plano de treino")
        print("  [2] Ver histórico de planos")
        print("  [3] Calcular 1RM (sem salvar)")
        print("  [4] Exportar planos para .txt")
        print("  [0] Sair")
        print("═" * 55)

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            configurar_treino(dados)
        elif opcao == "2":
            ver_historico(dados)
        elif opcao == "3":
            calcular_1rm_avulso()
        elif opcao == "4":
            exportar_txt(dados)
        elif opcao == "0":
            print("\n  Bom treino! 💪\n")
            break
        else:
            print("  ⚠ Opção inválida.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()