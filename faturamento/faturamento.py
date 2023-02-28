import json

with open('targetsistemas-test/faturamento/faturamento.json', 'r') as f:
    faturamento = json.load(f)
    
menor_faturamento = faturamento[0]['valor']
maior_faturamento = faturamento[0]['valor']
soma_faturamento = 0
num_dias = 0

for dia in faturamento: 
    valor = dia['valor']
    
    if valor < menor_faturamento: 
        menor_faturamento = valor    
    if valor > maior_faturamento:
        maior_faturamento = valor
        
    if valor > soma_faturamento / len(faturamento):
        num_dias += 1
        
    if valor != 0:
        soma_faturamento += valor
        
media_faturamento = soma_faturamento / num_dias

print('Menor faturamento: R$ {:.2f}'.format(menor_faturamento))
print('Maior faturamento: R$ {:.2f}'.format(maior_faturamento))
print('Número de dias com faturamento acima da média mensa: {}'.format(num_dias))
print('Média mensal de faturamento: R$ {:.2f}'.format(media_faturamento))