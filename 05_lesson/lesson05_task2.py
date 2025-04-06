from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/dynamicid")
    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()
finally:
    driver.quit()
