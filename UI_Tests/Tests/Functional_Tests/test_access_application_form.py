import pytest
from selenium import webdriver
from .PageObject import Page_form as page


@pytest.mark.acceptance_tests
def test_access_application():
    """
    Tests access application. Open the politician application form and verifies that the driver access to the correct page
    by verifying the title of the web page
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    #Load the main page. In this case the home page of the politician app
    main_page = page.MainPage(driver)
    #Checks if the word "Have fun testing" is in title
    assert main_page.is_title_matches(), "The page title doesn't match"

    driver.close()