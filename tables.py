from ast import Delete
from dataclasses import dataclass
from email import header
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
        driver.find_element(By.LINK_TEXT,'Sortable Data Tables').click()
        
    def test_tables(self):
        driver = self.driver
        
        
        table_data=[[] for i in range(5)]
        print(table_data)
        
        for i in range (5):
            header = driver.find_element(By.XPATH,f'//*[@id="table1"]/thead/tr/th[{i+ 1}]/span')
            table_data[i].append(header.text)
            
            for j in range(4):
                row_data = driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{j+1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)