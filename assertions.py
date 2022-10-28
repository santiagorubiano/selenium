import unittest
from selenium import webdriver
# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
# sirve como un excepcion para nuestros assertions cuando queramos validad la precencia de un elemento
from selenium.common.exceptions import NoSuchElementException
class AssertionsTest(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()

    def test_search(self):
        self.assertTrue(self.is_element_present(By.NAME,'q'))
        
    def test_account(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME,'account-cart-wrapper'))
        
   
   
    def tearDown(self):
        self.driver.quit()
        # nos permite encontrar a los elementos,how nos dice el tipo de selector y what el valor que tiene 
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=  how, value= what)
        except NoSuchElementException():
            self.driver.close()
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)