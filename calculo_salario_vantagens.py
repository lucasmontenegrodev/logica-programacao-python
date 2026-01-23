salario_base = float(input('Digite o seu salario liquido:'))
print('O seu salario bruto é:', salario_base,)
print('O seu salario com vantagens é:' , salario_base + (salario_base * 0.10))
print('O seu salario com descontos é:' , salario_base - (salario_base * 0.05))
salario_liquido = salario_base + (salario_base * 0.10) - (salario_base * 0.05)
print('O seu salario liquido é:', salario_liquido)
print('Se investir na poupança irá receber:' , salario_liquido * 0.05  , ' de juros')
juros = salario_liquido * 0.05
print('Totalizando o valor de:', salario_liquido + juros, 'em 1 mes')