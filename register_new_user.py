#  me permite utlizar time.sleep()
import time
import unittest
from selenium import webdriver


# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
# sirve como un excepcion para nuestros assertions cuando queramos validad la precencia de un elemento
from selenium.common.exceptions import NoSuchElementException
class Register_new_user(unittest.TestCase):
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
        
    def test_new_user(self):
        driver=self.driver
        driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT,'Log In').click()
        
        create_account_buttom=driver.find_element(By.XPATH,'//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_buttom.is_displayed() and create_account_buttom.is_enabled())
        create_account_buttom.click()
        
        self.assertEqual('Create New Customer Account', driver.title)
        firts_name  = driver.find_element(By.ID,'firstname')
        last_name = driver.find_element(By.ID,'lastname')
        email_address = driver.find_element(By.ID,'email_address')
        news_letter_suscription= driver.find_element(By.ID,'is_subscribed')
        password = driver.find_element(By.ID,'password')
        confirm_password = driver.find_element(By.ID,'confirmation')
        submit_buttom = driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/button/span/span')
        
        self.assertTrue(firts_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_suscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_buttom.is_enabled())
        
        firts_name.send_keys('Test')
        time.sleep(1)
        last_name.send_keys('Test')
        time.sleep(1)
        email_address.send_keys('test@testmail.com')
        time.sleep(1)
        password.send_keys('Test12345')
        time.sleep(1)
        confirm_password.send_keys('Test12345')
        time.sleep(1)
        submit_buttom.click()
        
        
            
        
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
        # nos permite encontrar a los elementos,how nos dice el tipo de selector y what el valor que tiene 
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(By = how, value= what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)