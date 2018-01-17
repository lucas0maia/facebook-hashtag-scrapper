# WebScrapper para hashtags públicas do Facebook
# A API não permite mais fazer esse tipo de consulta
# A função devolve uma lista, nesse caso uso a biblioteca pandas para salvar em csv
#Ler nota a respeito do registro das datas de postagem

#Por: Lucas Cavalcanti Maia - Estudante de Jornalismo interessado em jornalismo de dados


#import sys
#import date_converter
#import datetime
import time
from selenium import webdriver
import pandas
import json
import requests

def buscahashtags(hashtag, quantidadedeposts):

    def consultafb(usuario, post):
        id_app = '0000' #seu ID de aplicativo na api do facebook
        securtity_id = '0000' #seu ID de segurança na api do facebook
        TOKEN = id_app + '|' + securtity_id
        url = f'https://graph.facebook.com/v2.11/{usuario}_{post}?access_token={TOKEN}'
        conteudo = requests.get(url)
        testador =  conteudo.json()
        if 'created_time' in testador: 
            data = conteudo.json()['created_time']
            data = time.strptime(data[:19], "%Y-%m-%dT%H:%M:%S")
            data = time.strftime("%d/%m/%Y", data)
        else:
            data = "Sem Data"
        return(data)

    postagens = []
    driver = webdriver.Firefox() #É preciso baixar o geckodriver do Firefox e setar para o PATH do computador
    driver.get(f'https://www.facebook.com/hashtag/{hashtag}')
    for i in range(quantidadedeposts):
    
        nomedapessoa = driver.find_elements_by_class_name("_5pbw")
        conteudo = driver.find_elements_by_class_name("userContent")

        informacoes = driver.find_elements_by_xpath("//*[@class='_5bl2 _3u1 _41je']") #classe que contem informacoes do post
        informacoes = (informacoes[i].get_attribute('data-bt')) #atributo que possui um json com informacoes
        informacoes = json.loads(informacoes)
        idDapostagem = informacoes['id'] #pega o id da postagem a partir do json
        idDousuario = informacoes['owner_id']
        linkdopost = (f'https://www.facebook.com/{idDapostagem}')
        
        data = consultafb(idDousuario, idDapostagem)


        ###NOTA###
        #data = driver.find_elements_by_xpath("//*[@class='_5ptz']")
        #data = int(data[i].get_attribute('data-utime')) #PEGA A DATA ATRAVÉS DE SEU ATRIBUTO
        #data = date_converter.timestamp_to_datetime(data).strftime("%d/%m/%Y") #A DATA É EM FORMATO UNIX TIMESTAMP, AQUI ELA É CONVERTIDA PARA UM FORMATO LEGÍVEL

        #Esse modo de obter a data de postagem seria o ideal, porém o Facebook muda o nome da classe em determinados posts (há x horas) e isso faz com que algumas datas
        #fiquem trocadas. Por isso optei por utilizar a API para buscar as datas. Alguns posts acabam ficando sem data, mas isso é melhor que ter informação errada.
        #A próxima atualização será para corrigir isso.

        dicionariodopost = {"Nome":nomedapessoa[i].text, "Post":conteudo[i].text, "Link":linkdopost, "Data":data}
        postagens.append(dicionariodopost)
        
    
        #print(nomedapessoa[i].text) #prints de teste
        #print(conteudo[i].text)
        #print(linkdopost)
        #print(data)
    
    
        driver.execute_script("window.scrollTo(0, 100000)") #script para rolagem de tela
        time.sleep(2.5) #Você pode alterar o tempo de delay. Um tempo muito baixo vai dar erro
    return(postagens)

dadoshashtags = pandas.DataFrame(buscahashtags("choquedecultura", 20)) #Colocar entre aspas a palavra a ser buscada sem '#', e o numero de postagens que se deseja
dadoshashtags.to_csv('choquedecultura.csv')
