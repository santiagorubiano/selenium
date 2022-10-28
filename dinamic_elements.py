from ast import Delete
import unittest
from xml.dom.minidom import Element
from selenium import webdriver
 #By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
#submodulo  para usar el dropdown
import time
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service

class AddRemoveElements(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Disappearing Elements').click()
        
    def test_dinamic_element(self):
        driver = self.driver
        
        options=[]
        menu=5
        tries=1
        
        while len(options) < 5:
            options.clear()
            
            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH,f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                    
                except:
                    print(f'Option number {i + 1} is NOT FOUND' )
                    tries += 1
                    driver.refresh()
                    
        print(f'finished in {tries} tries')
                    

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)