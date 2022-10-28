import unittest
from selenium import webdriver


# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
# sirve como un excepcion para nuestros assertions cuando queramos validad la precencia de un elemento
from selenium.common.exceptions import NoSuchElementException
class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.implicitly_wait(40)
        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        
        
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
    def test_search_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        products= driver.find_elements(By.XPATH,'//div[@class = "product-info"]/h2[@class="product-name"]/a')
        self.assertEqual(1, len(products))
   
    def tearDown(self):
        self.driver.quit()
        # nos permite encontrar a los elementos,how nos dice el tipo de selector y what el valor que tiene 
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(By = how, value= what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)