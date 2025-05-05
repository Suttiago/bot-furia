from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_next_games():
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

    jogos = soup.find_all('a', class_='MatchCardSimple__MatchContainer-sc-wcmxha-0 duKvby')
    base_url = "https://draft5.gg"
    jogos_texto = ""

    for jogo in jogos:
        link = base_url + jogo['href']

        # Captura os nomes dos times
        times = jogo.find_all('div', class_='MatchCardSimple__TeamNameAndLogo-sc-wcmxha-40')
        if len(times) >= 2:
            time_a = times[0].find('span').text.strip()
            time_b = times[1].find('span').text.strip()
            confronto = f"{time_a} vs {time_b}"
        else:
            confronto = "Confronto ainda não disponível"

        # Captura a data/hora do jogo
        data_hora = jogo.find('div', class_='MatchCardSimple__DateTime-sc-wcmxha-10')
        if data_hora:
            data_hora_texto = data_hora.text.strip()
        else:
            data_hora_texto = "Data/Hora não disponível"

        jogos_texto += f"🏆 {confronto}\n🕒 {data_hora_texto}\n🎮 {link}\n\n"

    driver.quit()

    # Verifica se há jogos disponíveis
    if not jogos_texto.strip():
        return "Nenhum jogo futuro encontrado no momento."
    return jogos_texto