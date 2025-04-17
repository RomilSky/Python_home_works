import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    zip_alert = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_alert.get_attribute("class")

    valid_fields_ids = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in valid_fields_ids:
        alert_div = driver.find_element(By.ID, field_id)
        assert "alert-success" in alert_div.get_attribute("class")
