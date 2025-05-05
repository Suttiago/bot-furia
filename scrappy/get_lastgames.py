from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_last_games():
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

    jogos = soup.find_all('a', class_='MatchCardSimple__MatchContainer-sc-wcmxha-0 kSyLSS')

    base_url = "https://draft5.gg"
    jogos_texto = ""

    for jogo in jogos:
        link = base_url + jogo['href']

        placares = jogo.find_all('div', class_='MatchCardSimple__Score-sc-wcmxha-15')
        placar_final = f"{placares[0].text.strip()}x{placares[1].text.strip()}"

        times = jogo.find_all('div', class_='MatchCardSimple__TeamNameAndLogo-sc-wcmxha-40')
        if len(times) >= 2:
            time_a = times[0].find('span').text.strip()
            time_b = times[1].find('span').text.strip()
            confronto = f"{time_a} vs {time_b}"
        else:
            confronto = "Confronto ainda não disponível"

        jogos_texto += f"🏆 {confronto} - {placar_final}\n🎮 {link}\n\n"

    driver.quit()
    return jogos_texto

