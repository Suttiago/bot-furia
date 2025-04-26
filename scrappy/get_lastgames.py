from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def get_games():
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
    jogos = soup.find_all('a', class_='MatchCardSimple__MatchContainer-sc-wcmxha-0 kSyLSS')
    base_url = "https://draft5.gg"
    jogos_link = " "
    for jogo in jogos:
        link = base_url + jogo['href']
        jogos_link += f"🎮  {link} \n"
        
    driver.quit()        
    return jogos_link
get_games()