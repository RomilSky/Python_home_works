import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка итоговой суммы заказа")
@allure.description("Добавление товаров в корзину, оформление заказа и проверка общей суммы.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_total(browser):
    with allure.step("Открываем страницу магазина"):
        browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    with allure.step("Вход в систему"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары и переходим к оформлению"):
        inventory_page.add_items_to_cart()
        inventory_page.go_to_cart()
        cart_page.checkout()

    with allure.step("Заполняем форму оформления заказа"):
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Проверяем итоговую сумму"):
        total = checkout_page.get_total()
        assert "$58.29" in total, f"Ожидалось $58.29, получено {total}"
