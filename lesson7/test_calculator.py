from selenium import webdriver
from lesson7.calculator_page import CalculatorPage


def test_calc_result():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()
    assert result == "15"

    driver.quit()
