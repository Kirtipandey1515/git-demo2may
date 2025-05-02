import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseSauce:
    def Login(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()


#sdet1 did some changes