import pytest
from selenium import webdriver
from .PageObject import Page_form as page


@pytest.mark.acceptance_tests
def test_add_politician():
    """
    Tests add_politician. Open the politician application form and writes a valid name in to full name filed
    and verifies that the name of the politician was added correctly and its shown in the modal window after click on save.
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
    driver.implicitly_wait(30)

    # print to see in console the text of the modal
    print(main_page.get_value_from_modal())

    # Verifies if the name of the politician was added correctly
    assert "Cristhian" in main_page.get_value_from_modal(),"Name doesn't match"

    driver.close()

