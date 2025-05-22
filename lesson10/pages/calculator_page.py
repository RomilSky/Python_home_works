from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Страница калькулятора"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(driver, 50)

    def set_delay(self, value: str) -> None:
        """Установить задержку в мс"""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, label: str) -> None:
        """Нажать кнопку с текстом label"""
        button = self.driver.find_element(By.XPATH, f"//span[text()='{label}']")
        button.click()

    def get_result(self) -> str:
        """Получить результат вычисления"""
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "screen")))
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.driver.find_element(By.CLASS_NAME, "screen").text
