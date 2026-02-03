import secrets

# --- PEDE TAMANHO ---
while True:
    try:
        tamanho = int(input('Digite o número de caracteres da sua senha: '))
        if tamanho <= 0:
            print('O tamanho da senha deve ser positivo.\n')
        else:
            break
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.\n')

# --- PEDE CARACTERES ESPECIAIS ---
while True:
    especial = input('Deseja que sua senha tenha caracteres especiais? (s/n): ').strip().lower()
    if especial in ('s', 'n'):
        break
    else:
        print('Opção inválida. Digite "s" ou "n".\n')

# --- AVALIA FORÇA ---
if tamanho <= 6:
    print('Senha fraca!')
elif tamanho >= 10:
    print('Senha forte!')

# --- GERA SENHA ---
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
if especial == 's':
    caracteres += '!@#$%^&*()'

senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
print(f'\nSenha gerada: {senha}')
