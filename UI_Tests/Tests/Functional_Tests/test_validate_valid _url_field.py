import pytest
from selenium import webdriver
from .PageObject import Page_form as page


@pytest.mark.acceptance_tests
def test_validate_valid_url_field_case1():
    """
    Tests valida url field. Open the politician application form and writes a valid URL.
    Expected result: The field text should be valid
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets all the text fields of the form

    main_page.set_url_text_to_field("www.complyadvantage.com")
    # Verifies if the name of the politician was added correctly
    assert not main_page.is_invalid_url()

@pytest.mark.acceptance_tests
def test_validate_valid_url_field_case2():
    """
    Tests valida url field. Open the politician application form and writes an invalid URL. String
    Input data: String: dqdqdqwdqwdq
    Expected result: The modal should be INVALID
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets all the text fields of the form

    main_page.set_url_text_to_field("dqdqdqwdqwdq")
    # Verifies if the name of the politician was added correctly
    assert main_page.is_invalid_url()

@pytest.mark.acceptance_tests
def test_validate_valid_url_field_case3():
    """
    Tests valida url field. Open the politician application form and writes an invalid URL. just numbers
    Input data: INT: 24243423
    Expected result: The modal should be INVALID
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets all the text fields of the form

    main_page.set_url_text_to_field("24243423")
    # Verifies if the name of the politician was added correctly
    assert main_page.is_invalid_url()

@pytest.mark.acceptance_tests
def test_validate_valid_url_field_case4():
    """
    Tests valida url field. Open the politician application form and writes an invalid URL. String + dot
    Input data: INT: wwww.
    Expected result: The modal should be INVALID
    """
    driver = webdriver.Chrome()
    driver.get("http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/")

    # Load the main page. In this case the home page of the politician app

    main_page = page.MainPage(driver)

    # Sets all the text fields of the form

    main_page.set_url_text_to_field("wwww.")
    # Verifies if the name of the politician was added correctly
    assert main_page.is_invalid_url()