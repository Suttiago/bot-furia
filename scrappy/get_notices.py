from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

url = 'https://draft5.gg/equipe/330-FURIA'

options.add_experimental_option("prefs", prefs)
options.add_argument("--headless")
driver = webdriver.Chrome(options= options, service= service)

driver.get(url)
