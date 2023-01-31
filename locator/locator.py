from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = driver.find_element(By.ID,"name")
name.send_keys("Bibek Bhattarai")

time.sleep(3)

confirm = driver.find_element(By.ID,'confirmbtn')
confirm.click()

time.sleep(3)

driver.quit()
