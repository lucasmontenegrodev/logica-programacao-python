print('Digite a sua idade em anos, meses e dias')
ano = int(input('Anos:'))
mes = int(input('Meses:'))
dia = int(input('Dias:'))
ano = ano * 365
mes = mes * 30
dia = dia * 1
dias_de_vida = ano + mes + dia
print('Voce ja viveu ', dias_de_vida, ' dias')
