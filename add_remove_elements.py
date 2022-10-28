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
        driver.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        
    def test_add_remove(self):
        driver = self.driver
        
        element_added = int(input('How many elements will yoy add? '))
        element_removed = int(input('How many elements will yoy remove? '))
        total_elements = element_added -  element_removed
        
        add_buttom = driver.find_element(By.XPATH,'//*[@id="content"]/div/button')
        
        time.sleep(3)
        
        for i in range (element_added):
            add_buttom.click()
            
        for i in range(element_removed):
            try:
                Delete_buttom = driver.find_element(By.XPATH,'//*[@id="elements"]/button')
                Delete_buttom.click()
            except:
                print("you're trying to delet more elements the the exist")
                
        if total_elements > 0:
            print(f"there {total_elements} elements on screem") 
        else:
            print("there 0 elements on screem")
            
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)