from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Страница логина"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        """Вход в систему"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
