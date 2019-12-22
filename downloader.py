'''
# Ve a esta pagina -> https://cookidoo.es/search/es-ES, elige las categorías y que quieres filtrar
# Luego copia el url y pegalo abajo entre comillas
# ejemplo: pagina = "https://cookidoo.es/search/es-ES?query=*&countries=es&sortby=title"
'''
pagina = "https://cookidoo.es/search/es-ES?query=*&countries=au&sortby=title"
usuario = ""
contrasena = ""

###### NO MODIFICAR A PARTIR DE AQUÍ ############################################
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ids = []
driver = webdriver.Firefox()
driver.get("https://cookidoo.es/foundation/es-ES")
time.sleep(1)

driver.find_element_by_tag_name('body').send_keys(Keys.TAB + Keys.ENTER)
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.TAB * 6 + Keys.ENTER)
wait = WebDriverWait(driver, 10)
email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
email.send_keys(usuario)
password = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
password.send_keys(contrasena + Keys.ENTER)
wait.until(EC.title_contains("Cookidoo"))

for k in range(20):
    i = 0
    if k < 9:
        driver.get("{}&page={}&categories=VrkNavCategory-RPF-00{}".format(pagina,i,k+1))
    else:
        driver.get("{}&page={}&categories=VrkNavCategory-RPF-0{}".format(pagina,i,k+1))
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'link--alt')))
    elementos = driver.find_elements_by_tag_name("core-tile")

    while len(elementos) > 7:
        for j in elementos:
            receta = j.get_attribute("id")
            if id not in ids:
                ids.append(receta)
        i += 1
        if k < 9:
            driver.get("{}&page={}&categories=VrkNavCategory-RPF-00{}".format(pagina,i,k+1))
        else:
            driver.get("{}&page={}&categories=VrkNavCategory-RPF-0{}".format(pagina,i,k+1))
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'link--alt')))
        elementos = driver.find_elements_by_tag_name("core-tile")
        main_window = driver.current_window_handle

for receta in ids:
    driver.get("https://cookidoo.es/recipes/recipe/es-ES/{}".format(receta))
    f = open("C:\\Users\\Asier\\Desktop\hey\\recipes\\recipe\\es-ES\\{}.html".format(receta), "wb")
    f.write((driver.page_source).encode('utf-8'))
    f.close()