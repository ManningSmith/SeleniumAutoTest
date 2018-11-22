import unittest
from selenium import webdriver
import time
from POMDemo.Pages.Login import LoginPage
from POMDemo.Pages.HomePage import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/George.Smith/PycharmProjects/Selenium/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()

        try:
            homepage.click_logout()

        except:
            print('Language not English - Unable to log out...')

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')


if __name__ == '__main__':
    unittest.main()
