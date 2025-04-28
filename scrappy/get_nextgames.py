from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_games():
    url = 'https://draft5.gg/equipe/330-FURIA'
    options = Options()
    service = Service()
    prefs = {}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=service)

    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Procurar a mensagem de "Nenhuma partida encontrada"
    empty_message = soup.find('p', class_='EmptyState__EmptyStateText-sc-12we3sr-1 Bxkn')

    if empty_message:
        jogos_texto = empty_message.text.strip()
    else:
        jogos_texto = "✅ Existem partidas cadastradas."  # ou fazer a busca normal dos jogos

    driver.quit()
    return jogos_texto

# Teste
print(get_games())
