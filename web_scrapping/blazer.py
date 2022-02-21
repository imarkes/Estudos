from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://blaze.com/pt/games/crash'
options = Options()
options.add_argument('window-size=300,400')
driver = webdriver.Chrome(options=options)
driver.get(url)

numero = driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
VALOR = numero.replace('X', '')
sorteados = []
while True:
    numero2 = driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
    if numero2 != VALOR:
        sorteados.append(numero2.replace('X', ''))
        print(VALOR, numero2)
        print('salvou no banco')
        print(sorteados)
        VALOR = numero2
    sleep(4)

driver.quit()