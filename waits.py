import unittest
from selenium import webdriver
 #By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
 # para seleccionar elementos de la web con sus selectores
from selenium.webdriver.common.by import By
#submodulo  para usar el dropdown
import time
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
#Importar esperar explicitas
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com  ")
        driver.maximize_window()
        
    def test_account_link(self):
        #Cuentas del sitio
        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver,10).until (lambda s : s.find_element(By.ID,'select-language').get_attribute('lenght')== '3')
         #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()
    def test_create_new_customer(self):
        self.driver.find_element(By.LINK_TEXT,'ACCOUNT').click()
        
        my_account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By.LINK_TEXT,'My Account'))
        my_account.click()
        
        create_account_buttom = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(By.LINK_TEXT,'CREATE AN ACCOUNT'))
        create_account_buttom.click()
        
        WebDriverWait(self.driver,10).until(EC.title_contains('Create New Customer Account'))
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)