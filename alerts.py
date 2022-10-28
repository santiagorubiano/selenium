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
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        
    def test_compare_products_remo(self):
        driver = self.driver
        #buscamos el buscador
        search_field = driver.find_element(By.NAME,'q')
        #limpoamos el buscador 
        search_field.clear()
        #escribimos 'tee' en el buscador'
        search_field.send_keys('Tee')
        #inicamos la busqueda
        search_field.submit()
        #buscamos el boton de add to compare y le damos click
        driver.find_element(By.CLASS_NAME,'link-compare').click()
        #buscamos el boton de clear all y le damos click
        driver.find_element(By.LINK_TEXT,'Clear All').click()    
        #enfocamos la atencion al alert   
        alert = driver.switch_to.alert
        #guardamos el testo del alert en la variable alert_text
        alert_text = alert.text
        #comparamos el texto que nos arroja el alert con el contenido de alert_text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        time.sleep(10)
        alert.accept

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)