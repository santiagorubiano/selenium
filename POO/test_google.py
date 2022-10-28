import unittest
from selenium import webdriver
 #By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
from google_page import GooglePage
class SearchDDT(unittest.TestCase):
    @classmethod
    def setUp(cls):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.maximize_window()
    
    def test_search_ddt(cls):
        google = GooglePage(cls.driver)
        google.open()
        google.search('platzi')
        
        cls.assertEqual('platzi', google.keyword)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)