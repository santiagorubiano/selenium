import unittest
from selenium import webdriver
 #By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
#submodulo  para usar el dropdown
import time
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service

class Compare_products(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()
        
    def test_browser_navigation(self):
        driver =self.driver
        #Buscamos el buscador de google
        search_field = driver.find_element(By.NAME,'q')
        #limpiamos e buscador
        search_field.clear()
        #escribimos 'platzi' 
        search_field.send_keys('platzi')
        #le damos en iniciar la busqueda
        search_field.submit()
        time.sleep(3)
        # para atras
        driver.back()
        time.sleep(3)
        #adelante
        driver.forward()
        time.sleep(3)
        #refrescar
        driver.refresh()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)