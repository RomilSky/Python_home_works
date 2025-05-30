from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Страница корзины."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 10 секунд на появление и активацию кнопки «Checkout»
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> None:
        """
        Нажимает кнопку «Checkout».

        Метод ждёт, пока элемент станет кликабельным,
        что гарантирует, что страница полностью прогрузилась
        и товары действительно добавлены в корзину.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
