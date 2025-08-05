import requests


lista = ['EUR', 'USD', 'BRL']

print('=-' * 10)
print('Conversor de Moedas')
print('=-' * 10)

print('Qual a moeda de origem?')
print('\n0- Euro \n1- Dolar Americano \n2- Real Brasileiro')

opcao = input('Escolha a opção:')

if opcao == '0':
    de = 'EUR'
elif opcao == '1':
    de = 'USD'
else:
    de = 'BRL'


print('Qual valor deseja converter?')
print('\nPara qual valor deseja converter? \n0- Eur \n1- Dolar  \n2- Brl')
opcao_cnvrt = input('Escolha a opção:')

if opcao_cnvrt == '0':
    para = 'EUR'
elif opcao_cnvrt == '1':
    para = 'USD'
else:
    para = 'BRL'
print()

# request
valor = float(input("quanto dinheiro queres converter? "))
cotacao = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(de+'-'+para))
cotacao = cotacao.json()
cotacao_moeda = float(cotacao['{}'.format(de+para)]['bid'])

r = round(valor * cotacao_moeda,2)
print('O valor convertido é de',r,para)