import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
#submodulo  para usar el dropdown
from selenium.webdriver.support.ui import Select
import time
# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service

class Language_option(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        
    def test_search_language(self):
        #el orden respeta como aparecen en la página
        exp_opt = ['English', 'French', 'German']
        #para almacenar las opciones que elijamos
        act_opt = []
            #para acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element(By.ID,'select-language'))
        #para comprobar que si esté la cantidad de  opciones correcta
		#'options' permite ingresar directamente a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))
        # se realiza un cliclo 'for' para agregar las opciones a la lisra act_opt y 
        # soño se agrega el texto utilizando .text
        for option in select_language.options:
            act_opt.append(option.text)
        #verifico que la lista de opciones disponibles y activas sean indénticas
        self.assertListEqual(exp_opt,act_opt)
        #vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English',select_language.first_selected_option.text)
        #seleccionamos "German" por el texto visible
        
        #verificamos que el sitio cambio a Alemán
        select_language.select_by_visible_text('German')
        #verificamos que el sitio cambio a Alemán
		#preguntamos a selenium si la url del sitio contiene esas palabras
        self.assertTrue('store=german' in self.driver.current_url)
        
        select_language = Select(self.driver.find_element(By.ID,'select-language' ))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)