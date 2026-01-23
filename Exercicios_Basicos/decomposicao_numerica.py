numero = -1
while numero < 0:
    numero = int(input('Digite um numero inteiro positivo:'))
    if numero < 0:
        print('Numero invalido! Tente novamente.')
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
print(f'centena: {centena}, dezena: {dezena}, unidade: {unidade}')

