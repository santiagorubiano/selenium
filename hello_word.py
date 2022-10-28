from http.server import executable
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class helloWord(unittest.TestCase):
    @classmethod
    def setUp(cls) :
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)
        
    def test_Hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')
    
    def visit_wikipedia(cls):
        cls.driver.get('https://wikipedia.org')

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    
if __name__ == '__main__':
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output='resportes', report_name='hello-word-report'))
        
    