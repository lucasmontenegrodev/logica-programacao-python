fibonnaci = [0, 1]
for i in range(2, 20):
    next_value = fibonnaci[i-1] + fibonnaci[i-2]
    fibonnaci.append(next_value)
print(fibonnaci)
n = int(input("Digite um numero que eu irei responder se é um numero fibonnaci: "))
if n in fibonnaci:
    index = fibonnaci.index(n)
    print(f"O numero {n} é um numero fibonnaci e seus 10 seguintes numeros são:")
    for i in range(index + 1, min(index + 11, len(fibonnaci))):
        print(fibonnaci[i])
else:
    print(f"O numero {n} não é um numero fibonnaci.")