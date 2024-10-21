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
        assert self.driver.find_element(By.XPATH, "//input[@class='inputs ui-autocomplete-input']").get_attribute(
            "value") == "Dominica"

    def test_static_dropdown(self):
        log = self.getLogger()
        # Dropdown
        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option1")
        log.info("Dropdown value selected")

        time.sleep(2)

    def test_checkbox(self):

        log = self.getLogger()

        self.driver.find_elements(By.NAME, "checkBoxOption1")
        self.driver.find_element(By.NAME, "checkBoxOption3")
        log.info("Checkbox option 1 and option 3 selected")

    def test_mouse_hover(self):

        log = self.getLogger()

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, "mousehover")).perform()
        action.context_click(self.driver.find_element(By.LINK_TEXT, "Top")).perform()
        time.sleep(5)
        log.info("Hover on Mouse Hover button and right click on Top option")

    def test_switch_window(self):

        log = self.getLogger()

        self.driver.find_element(By.XPATH, "//button[@onclick='openWindow()']").click()

        windowsOpened = self.driver.window_handles

        self.driver.switch_to.window(windowsOpened[1])
        grabText = self.driver.find_element(By.LINK_TEXT, "Access all our Courses").text

        assert grabText == "Access all our Courses"

        log.info("Switched to another window")
    @pytest.mark.Tab
    def test_switch_Tab(self):

        log = self.getLogger()

        self.driver.find_element(By.ID, "opentab").click()

        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[1])
        time.sleep(5)
        grabText = self.driver.find_element(By.LINK_TEXT, "Global Academy").text
        log.info("Switching to another Tab, intentionally failing this test case to verify screenshot captured")
        assert grabText == "Global"

        # Intentionally Fail the test case in assertion to test screenshot in report

    def test_Alert(self):
        log = self.getLogger()
        name = "Abhijeet"
        self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)

        self.driver.find_element(By.ID, "alertbtn").click()
        alert = self.driver.switch_to.alert
        alertText = alert.text
        time.sleep(5)
        assert name in alertText
        alert.accept()

        self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
        self.driver.find_element(By.ID, "confirmbtn").click()
        alert = self.driver.switch_to.alert
        time.sleep(5)
        alert.dismiss()
        log.info("Switching to another alert")

    def test_ElementDisplayed(self):

        log = self.getLogger()

        self.driver.find_element(By.ID, "hide-textbox").click()
        self.driver.find_element(By.ID, "show-textbox").click()

        self.driver.find_element(By.XPATH, "//input[@class='inputs displayed-class']").send_keys("Abhijeet")
        time.sleep(5)
        log.info("testing to hide and show element")

    @pytest.mark.screen
    def test_scroll_screenshot(self):

        log = self.getLogger()

        self.driver.execute_script("window.scrollBy(0,500);")
        time.sleep(2)
        self.driver.get_screenshot_as_file("screenShot1.png")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(2)
        self.driver.get_screenshot_as_file("screenShot2.png")

        log.info("Testing how to scroll and take screenshot")

        print(self.driver.title)

    @pytest.mark.frames
    def test_frames(self):

        log = self.getLogger()
        # switching to frames
        self.driver.switch_to.frame("courses-iframe")

        self.driver.find_element(By.XPATH, "//a[@class='theme-btn register-btn']").click()
        time.sleep(3)

        # switching to default content
        self.driver.switch_to.default_content()
        grabText = self.driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").text

        assert grabText == "Free Access to InterviewQues/ResumeAssistance/Material"

        log.info("Switching to frames and back to default content")

