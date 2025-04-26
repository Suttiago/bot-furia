from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def get_notices():
    url = 'https://draft5.gg/equipe/330-FURIA'
    options = Options()
    service = Service()
    prefs = {}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options= options, service= service)

    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    noticias = soup.find_all('a', class_='NewsCardSmall__NewsCardSmallContainer-sc-1q3y6t7-0')
    
    base_url = "https://draft5.gg"
    for noticia in noticias:
        titulo = noticia.find('p').text.strip()
        link = base_url + noticia['href']
        noticas_texto = f"📰 {titulo} \n {link} \n"
    driver.quit()        
    return noticas_texto
