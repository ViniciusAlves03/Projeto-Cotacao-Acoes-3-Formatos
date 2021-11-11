import requests
from bs4 import BeautifulSoup
from unicodedata import normalize


url_base = 'https://www.infomoney.com.br/cotacoes/'

empresa_nome = input('Qual o nome da empresa?')
empresa_simbolo = input('Qual o simbolo da ação da empresa?')

empresa_nome_formatada = normalize('NFKD', empresa_nome).encode('ASCII','ignore').decode('ASCII') # Para retirar a acentuuação das letras!
site_formatado = url_base + empresa_nome_formatada + '-' + empresa_simbolo + '/'

response = requests.get(site_formatado)

site = BeautifulSoup(response.text, 'html.parser')

acao = site.find('div', attrs={'class':"fill-lightgray border-b"})

preco  = acao.find('div', attrs={'class':'value'}).find('p')

print(f'Empresa: {empresa_nome.upper()}\nSímbolo: {empresa_simbolo.upper()}\nPreço: R${preco.text}\nPara mais informações, acesse: {site_formatado}')
