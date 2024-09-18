from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Inicializar servicos
def execute():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service, options=options)
    navegador.maximize_window()
    wait = WebDriverWait(navegador, 40)


    url_login = 'https://github.com/'
    navegador.get(url_login)


    xpath = '/html/body/div[1]/div[4]/main/div[2]/div[2]/div/div/div[2]/h1/span'
    text = navegador.find_element(By.XPATH, xpath).text
    return text

