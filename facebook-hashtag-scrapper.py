# WebScrapper para hashtags p�blicas do Facebook
# A API n�o permite mais fazer esse tipo de consulta
# Essa � uma vers�o inicial. Posteriormente irei criar uma fun��o que facilite o trabalho de colocar os dados em csv.
#Por Lucas Cavalcanti Maia - Estudante de Jornalismo interessado em jornalismo de dados

from selenium import webdriver
import time
import re
driver = webdriver.Firefox()
driver.get('httpswww.facebook.comhashtagmeuamigosecreto')
for i in range(100)
    nomedapessoa = driver.find_elements_by_class_name(_5pbw)
    datadapostagem = driver.find_elements_by_class_name(timestampContent)
    conteudo = driver.find_elements_by_class_name(userContent)
    
    print(i,n)
    
    print(nomedapessoa[i].text)
    print(datadapostagem[i].text)
    print(conteudo[i].text)

    
    
    driver.execute_script(window.scrollTo(0, 100000))
    time.sleep(1.5)
