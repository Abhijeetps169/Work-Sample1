import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


# @pytest.mark.Usefixtures("setup")


class Test_one(BaseClass):


    def test_radio_button(self):
        log = self.getLogger()

        # radio button
        self.driver.find_element(By.XPATH, "//input[@value='radio1']").click()
        log.info("Selected first radio button")


    @pytest.mark.dyndrop
    def test_dynamic_dropdown(self):
        # Autosuggestion or Dynamic dropbox
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@class='inputs ui-autocomplete-input']").send_keys("In")
        time.sleep(4)
        countries = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")

        for country in countries:
            if country.text == "Dominica":
                country.click()
                break

        log.info("Selected \"Dominica\" country from Auto suggested dropdown")
        assert self.driver.find_element(By.XPATH, "//input[@class='inputs ui-autocomplete-input']").get_attribute("value") == "Dominica"

    def test_static_dropdown(self):
        log = self.getLogger()
        # Dropdown
        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option1")
        log.info("Dropdown value selected")

        time.sleep(2)

    @pytest.mark.check
    def test_checkbox(self):

        log = self.getLogger()

        self.driver.find_elements(By.NAME, "checkBoxOption1")
        self.driver.find_element(By.NAME, "checkBoxOption3")
        log.info("Checkbox option 1 and option 3 selected")

    @pytest.mark.action
    def test_mouse_hover(self):

        log = self.getLogger()

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID,"mousehover")).perform()
        action.context_click(self.driver.find_element(By.LINK_TEXT,"Top")).perform()
        time.sleep(5)
        log.info("Hover on Mouse Hover button and right click on Top option")

    #def test_switch_window(self):

        #log = self.getLogger()