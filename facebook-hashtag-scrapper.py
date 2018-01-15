# WebScrapper para hashtags públicas do Facebook
# A API não permite mais fazer esse tipo de consulta
# Essa é uma versão inicial. Posteriormente irei criar uma função que facilite o trabalho de colocar os dados em csv.
#Por: Lucas Cavalcanti Maia - Estudante de Jornalismo interessado em jornalismo de dados


import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#O código acima serve para 'traduzir' possiveis emojis nas postagens e evitar erros

from selenium import webdriver
import time
import re


quantidadedeposts = 100 # Alterar para a quantidade desejada
hashtag = ('foratemer') #alterar para a hashtag a ser pesquisada


driver = webdriver.Firefox() #É preciso baixar o geckodriver do Firefox e setar para o PATH do computador
driver.get(f'https://www.facebook.com/hashtag/{hashtag}')
for i in range(100):
    nomedapessoa = driver.find_elements_by_class_name("_5pbw")
    datadapostagem = driver.find_elements_by_class_name("timestampContent")
    conteudo = driver.find_elements_by_class_name("userContent")
    
    #Os prints são apenas um exemplo. O ideal é criar uma lista de dicionários para salvar em csv ou banco de dados

    print('\nPost número: ',i,"\n")
    
    print(nomedapessoa[i].text)
    print(datadapostagem[i].text)
    print((conteudo[i].text).translate(non_bmp_map)) #impede que a presenca de emojis cause erros

    
    
    driver.execute_script("window.scrollTo(0, 100000)")
    time.sleep(0.8) #Você pode alterar o tempo de delay. Um tempo muito baixo vai dar erro
