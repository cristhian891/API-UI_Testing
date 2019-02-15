from selenium.webdriver.common.by import By

class MainPageLocators (object):
    """This is the class for all locators in the main page form"""
    SAVE_BUTTON =(By.CLASS_NAME, 'btn')
    FULL_NAME_FIELD = (By.ID, 'fullName')
    COUNTRY_FIELD = (By.ID, 'country')
    YOB_DATE_PICK = (By.NAME, 'yob')
    POSITION_FIELD = (By.ID, 'position')
    URL_FIELD = (By.ID, 'url')
    RISK_LIST = (By.NAME, 'risk')
    INVALID_NAME = (By.CLASS_NAME,'invalid-feedback')
    MODAL_MESSAGE = (By.CLASS_NAME, 'modal-body')
    MODAL_BACK_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/button')
