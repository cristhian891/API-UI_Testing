from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from ..Locators.Main_Page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """Base class to intialize the base page that will be called from all"""

    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):


    def is_title_matches(self):
        """Verifies that the title contains the text """
        return "Have fun testing" in self.driver.title

    def click_on_save_button(self):
        """Triggers the save button in the form"""
        element = self.driver.find_element(*MainPageLocators.SAVE_BUTTON)
        element.click()

    def set_fullname_text_to_field(self, value):
        """Set value to the text field in the form"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.FULL_NAME_FIELD))
        element = self.driver.find_element(*MainPageLocators.FULL_NAME_FIELD)
        element.send_keys(value)

    def set_country_text_to_field(self, value):
        """Set value to the text field in the form"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.COUNTRY_FIELD))
        element = self.driver.find_element(*MainPageLocators.COUNTRY_FIELD)
        element.send_keys(value)

    def set_position_text_to_field(self, value):
        """Set value to the text field in the form"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.POSITION_FIELD))
        element = self.driver.find_element(*MainPageLocators.POSITION_FIELD)
        element.send_keys(value)

    def set_url_text_to_field(self, value):
        """Set value to the text field in the form"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.URL_FIELD))
        element = self.driver.find_element(*MainPageLocators.URL_FIELD)
        element.send_keys(value)

    def set_yob_text_to_field(self, value):
        """Set value to the text field in the form"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.YOB_DATE_PICK))
        element = self.driver.find_element(*MainPageLocators.YOB_DATE_PICK)
        element.send_keys(value)

    def get_value_from_modal(self):
        """Get the corresponded value from the modal alert"""
        """Gets the text of the specified object"""

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.MODAL_MESSAGE))
        element = self.driver.find_element(*MainPageLocators.MODAL_MESSAGE)
        return element.get_attribute("innerHTML")

    def select_risk(self, risk):
        """Select on the risk in the select element"""
        select = Select(self.driver.find_element(*MainPageLocators.RISK_LIST))
        select.select_by_visible_text(risk)

    def is_save_modal_visible(self):
        """ Return bollean if modal is visible """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*MainPageLocators.MODAL_BACK_BUTTON))
            element = self.driver.find_element(*MainPageLocators.MODAL_BACK_BUTTON)
            return element.is_displayed()

        except Exception as err:
            return False

    def click_modal_back_button(self):
        """Clicks on the back button in the modal and closes it"""
        element = self.driver.find_element(*MainPageLocators.MODAL_BACK_BUTTON)
        element.click()

    def is_invalid_url(self):
        """Return true if the the url field has a valid format, otherwise return false"""
        element = self.driver.find_element(*MainPageLocators.URL_FIELD)
        if element.get_attribute("class") == "is-valid form-control":
            return False
        elif element.get_attribute("class") == "is-invalid form-control":
            return True




