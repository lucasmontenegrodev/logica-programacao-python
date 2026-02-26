menor_altura = 0
soma_alturam = 0
contm = 0

for i in range(10):
    altura = float(input("Digite a altura da pessoa: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    if i == 0 or altura < menor_altura:
        menor_altura = altura

    if sexo == "M":
        soma_alturam += altura
        contm += 1

media_meninos = soma_alturam / contm 
print(f"A menor altura do grupo é: {menor_altura:.2f}")
print(f"A média da altura dos meninos é: {media_meninos:.2f}")

    
