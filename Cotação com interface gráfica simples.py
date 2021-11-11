import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import pygame
import sys

pygame.init()

janela = pygame.display.set_mode([500,500])

base_fonte =pygame.font.Font(None,28)
base_fonte_link =pygame.font.Font(None,22)

user_text =''
user_text2 ='' 
preco_final = ''
mais_info = ''

usuario_texto_lista = []
usuario_texto2_lista = []

input_rect = pygame.Rect(30,110,400,32)
input_rect2 = pygame.Rect(30,195,80,32)

cor_branca = pygame.Color(255,255,255)
cor_preta = pygame.Color(0,0,0)
cor_verde = pygame.Color(50,205,50)
cor_azul = pygame.Color(0,0,255)

imagem_fundo = pygame.image.load('imagem_de_fundo.png')

url_base = 'https://www.infomoney.com.br/cotacoes/'

contador_de_letras = 27
contador_de_letras2 = 9

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and contador_de_letras > 0:
            if event.key == pygame.K_DOWN:
                contador_de_letras -= contador_de_letras
            if event.key == pygame.K_BACKSPACE :
                user_text = user_text[:-1]
                contador_de_letras += 1
                usuario_texto_lista.pop()
            elif contador_de_letras > 1:
                user_text += event.unicode
                contador_de_letras -= 1
                usuario_texto_lista.append(user_text)
            texto1_formatado = usuario_texto_lista[-1]

        if event.type == pygame.KEYDOWN and contador_de_letras == 0 and contador_de_letras2 > 0:
            if event.key == pygame.K_BACKSPACE:
                user_text2 = user_text2[:-1]
                contador_de_letras2 += 1
                usuario_texto2_lista.pop()
            elif contador_de_letras2 > 1:
                user_text2 += event.unicode
                contador_de_letras2 -= 1
                usuario_texto2_lista.append(user_text2)
            texto2_formatado = usuario_texto2_lista[-1] 

        if event.type == pygame.KEYDOWN and len(usuario_texto2_lista) > 1:
            if event.key == pygame.K_DOWN:
                site_formatado = url_base + normalize('NFKD', texto1_formatado).encode('ASCII','ignore').decode('ASCII').replace(' ','-').lower() + '-' + normalize('NFKD', texto2_formatado).encode('ASCII','ignore').decode('ASCII').lower() + '/'
        
                response = requests.get(site_formatado)

                site = BeautifulSoup(response.text, 'html.parser')

                acao = site.find('div', attrs={'class':"fill-lightgray border-b"})

                preco  = acao.find('div', attrs={'class':'value'}).find('p')

                preco_final = 'R$'+ preco.text
                mais_info = site_formatado
                
    janela.fill(cor_preta)
    janela.blit(imagem_fundo,(0,0))

    pygame.draw.rect(janela,cor_branca,input_rect,2)
    pygame.draw.rect(janela,cor_branca,input_rect2,2)

    janela.blit(base_fonte.render(preco_final, True, cor_verde),(30,290))
    janela.blit(base_fonte_link.render(mais_info, True, cor_azul),(30,400))
    janela.blit(base_fonte.render(user_text, True, cor_branca),(input_rect.x + 5, input_rect.y + 5))
    janela.blit(base_fonte.render(user_text2, True, cor_branca),(input_rect2.x + 5, input_rect2.y + 5))
    
    pygame.display.flip()
