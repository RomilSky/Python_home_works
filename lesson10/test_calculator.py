import allure
from pages.calculator_page import CalculatorPage


@allure.title("Проверка калькуляции 7 + 8 = 15")
@allure.description("Убедиться, что калькулятор правильно считает выражение 7 + 8.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_result(browser):
    with allure.step("Открываем страницу калькулятора"):
        page = CalculatorPage(browser)

    with allure.step("Устанавливаем задержку и вводим выражение"):
        page.set_delay("45")
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получаем и проверяем результат"):
        result = page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
