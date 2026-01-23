      # Programa para calcular o 1Rm e registrar dias de treino

print('Configurando o seu treino!')
print('\nAgora responda quais os dias que você irá treinar com sim e não:')

dias_treino = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
meus_dias = []

for i in range(7):
      while True:
            resposta = input(f'Você vai treinar na {dias_treino[i]}? (sim/não): ').strip().lower()
            if resposta in ['sim', 'não', 'nao']:
                  if resposta == 'sim':
                        meus_dias.append(dias_treino[i])
                  break
            else:
                        print('Resposta inválida. Por favor, responda com "sim" ou "não".')
print('Seus dias de treino são:', ', '.join(meus_dias))

informacoes_treino = []

for dia in meus_dias:
    while True:
        try:
            qnt = int(input(f'\nQuantos exercícios você fará na {dia}? '))
            if qnt > 0:
                break
            print('Número inválido. Por favor, digite um número positivo.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')
    for i in range(qnt):
        while True:
            try:
                exercicio = input(f'Digite o exercicio da {dia}: ')
                um_rm = float(input(f'Qual é o seu 1Rm para {exercicio} em Kg? ').strip().replace(',', '.'))
                if um_rm > 0:
                    informacoes_treino.append((dia, exercicio, i + 1, um_rm))
                    break
                else:
                    print('Valor inválido. Por favor, digite um número positivo para o 1Rm.')
            except ValueError:
                print('Entrada inválida para o 1Rm. Por favor, digite um número válido.')

      # Montando as cargas e repetições do treino

print('\nAqui está o seu plano de treino baseado no seu 1Rm:')
for dia, exercicio, numero, um_rm in informacoes_treino:
            print(f'\n {exercicio}({um_rm}Kg) - {dia}:')
            print(f' Semana 1 (60%): {um_rm * 0.6:.2f} Kg x 12 - 15 repetições')
            print(f' Semana 2 (80%): {um_rm * 0.8:.2f} Kg x 8 - 10 repetições')
            print(f' Semana 3 (90%): {um_rm * 0.9:.2f} Kg x 6 - 8 repetições')
            print(f' Semana 4 (100%): {um_rm} Kg x 1 - 3 Repetições (Seu atual 1Rm!)')
            print(f' Semana de recuperação: {um_rm * 0.5:.2f} Kg x 15 - 20 repetições')
print('\nBom treino! Lembre-se de sempre aquecer e alongar antes e depois dos exercícios.')
