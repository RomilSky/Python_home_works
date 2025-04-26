from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_total():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_items_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_form("Иван", "Петров", "123456")
    total = checkout_page.get_total()

    assert "$58.29" in total

    driver.quit()
