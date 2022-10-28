from tkinter import E
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
 #By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
#submodulo  para usar el dropdown
from selenium.webdriver.support.ui import WebDriverWait
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
        driver.find_element(By.LINK_TEXT,'Dynamic Controls').click()
        
    def test_dinamic_controls(self):
        driver = self.driver
        checkbox=driver.find_element(By.XPATH,'//*[@id="checkbox"]/input')
        checkbox.click()
        
        remove_add_botton= driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button')
        remove_add_botton.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_botton.click()  
        
        enable_disable_button= driver.find_element(By.XPATH,'//*[@id="input-example"]/button')
        enable_disable_button.click()
        
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input-example"]/button')))
        
        text_area = driver.find_element(By.XPATH,'//*[@id="input-example"]/input')
        text_area.send_keys('Santiago Rubiano Murcia')
        
        enable_disable_button.click()
                    

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)