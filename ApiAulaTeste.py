import requests

url = requests.get('https://economia.awesomeapi.com.br/last/EUR-USD')
print(url)
cotacao = url.json()
print(cotacao)

cotacao_dolar = float(cotacao['EURUSD']['bid'])
valor = float(input("Qual o valor em Dolares deseja converter?"))
r = valor / cotacao_dolar
print("O valor convertido é de",round(r,2),"euros")
