import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


#@pytest.mark.Usefixtures("setup")
class Test_one(BaseClass):

    def test_e2e(self,setup):
        log = self.getLogger()
        self.driver.find_element(By.XPATH,"//input[@value='radio1']").click()
        log.info("Selected first radio button")
        time.sleep(5)
