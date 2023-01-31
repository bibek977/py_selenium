from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio = driver.find_element(By.XPATH,'//input[@value = "radio2"]')
radio.click()

checkbox = driver.find_element(By.XPATH,'//select/option[2]')
checkbox.click()

time.sleep(2)

driver.quit()