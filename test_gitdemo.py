import time

from page_objsauce.saucedemo import Saucedemo
from utilities.basesauce import BaseSauce


class Testsausedemo(BaseSauce):
    def test_saucedemo(self):
        self.Login()
        time.sleep(2)
        sau=Saucedemo(self.driver)
        sau.sauce()

#sample-line