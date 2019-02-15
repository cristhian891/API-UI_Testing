import pytest
from selenium import webdriver
from .PageObject import Page_form as page
import time


@pytest.mark.acceptance_tests
def test_mandatory_fields_case_1():
    """
    Tests add_politician. Open the politician application form and writes a fill all mandatories fields.
    Expected result: The modal should appear to the user
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets all the text fields of the form
    main_page.set_fullname_text_to_field("Cristhian Preciado")
    main_page.set_country_text_to_field("UK")
    main_page.set_yob_text_to_field("01/18/1989")
    main_page.set_position_text_to_field("Lead")
    main_page.set_url_text_to_field("www.complyadvantege.com")
    main_page.select_risk("HUGE")
    main_page.click_on_save_button()
    driver.implicitly_wait(10)

    time.sleep(6)
    # Verifies if the name of the politician was added correctly
    assert (main_page.is_save_modal_visible(), "All fields should be mandatory")
    driver.close()

@pytest.mark.acceptance_tests
def test_mandatory_fields_case2():
    """
    Tests add_politician. Open the politician application form and writes a fill ONLY: Fullname
    Expected result: The modal should appear to the user
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")
    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets only fullname fields of the form
    main_page.set_fullname_text_to_field("Cristhian Preciado")
    main_page.click_on_save_button()
    time.sleep(6)
    # Verifies if the name of the politician was added correctly
    assert not main_page.is_save_modal_visible(), "There is a missing a field so modal should not appear"
    driver.close()

@pytest.mark.acceptance_tests
def test_mandatory_fields_case3():
    """
    Tests add_politician. Open the politician application form and writes a fill ONLY: country
    Expected result: The modal should NOT appear to the user
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")
    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets only country fields of the form
    main_page.set_country_text_to_field("UK")
    main_page.click_on_save_button()
    time.sleep(6)
    # Verifies if the name of the politician was added correctly
    assert not main_page.is_save_modal_visible(), "There is a missing field so modal should not appear"
    driver.close()

@pytest.mark.acceptance_tests
def test_mandatory_fields_case4():
    """
    Tests add_politician. Open the politician application form and writes a fill ONLY: Yob
    Expected result: The modal should not appear to the user
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")
    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets only yob fields of the form
    main_page.set_yob_text_to_field("01/18/1989")
    main_page.click_on_save_button()
    time.sleep(6)
    # Verifies if the name of the politician was added correctly
    assert not main_page.is_save_modal_visible(), "There is a missing field so modal should not appear"
    driver.close()

@pytest.mark.acceptance_tests
def test_mandatory_fields_case5():
    """
    Tests add_politician. Open the politician application form and writes a fill ONLY: The Risk List
    Expected result: The modal should not appear to the user
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")
    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets only yob fields of the form
    main_page.select_risk("HUGE")
    main_page.click_on_save_button()
    time.sleep(6)
    # Verifies if the name of the politician was added correctly
    assert not main_page.is_save_modal_visible(), "There is a missing a field so modal should not appear"
    driver.close()