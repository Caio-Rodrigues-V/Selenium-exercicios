from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pydirectinput as pd
import pyautogui as pg
import csv


def iniciar_driver():
    chrome_options = Options()
    arguments = ["--start-maximized", "--incognito", "--window-size=1920,1080"]  # Adicionando '--start-maximized'
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": "C:\\Users\\caiov\\Downloads",
            "download.directory_upgrade": False,
            "download.prompt_for_download": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.automatic_downloads": 1,  # Corrigido: removido espaço após 'automatic_downloads'
        },
    )

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    return driver

def iniciar(driver):
    driver.get('https://www.bestbuy.com/')

def country_selecion(driver):
    pd.moveTo(842,494)
    sleep(3)
    pd.mouseDown()
    pd.mouseUp()
    sleep(3)
    
def pesquisa(driver):
    try:
        sleep(3)
        pesquisar = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))
        pesquisar.click()
        pesquisar.send_keys("pc gamer")
        pesquisar.send_keys(Keys.ENTER)
        sleep(3)
    except:
        print('nao foi possivel realizar a operação')    

def coletar_preco(driver):
    try:
        precos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "style-module_price__ql4Q1")))
        nome_arquivo = 'dados.csv'
        with open (nome_arquivo, 'w', newline = '') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for linha in precos:
                escritor_csv.writerow([linha.text])
    except:
        print('nao foi possivel realizar a operação')

      





def main():
    driver = iniciar_driver()
    iniciar(driver)
    country_selecion(driver)
    pesquisa(driver)
    coletar_preco(driver)
    driver.quit()

if __name__ == "__main__":
    main()