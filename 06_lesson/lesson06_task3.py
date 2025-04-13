from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
(driver.get
 ("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"))

wait = WebDriverWait(driver, 20)

wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4)

third_img = driver.find_elements(By.TAG_NAME, "img")[3]

wait.until(lambda d: third_img.get_attribute("src") != "")

print(third_img.get_attribute("src"))

driver.quit()
