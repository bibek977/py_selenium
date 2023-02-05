from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)

radio_btn = driver.find_element(By.CSS_SELECTOR,'input[value="radio1"]').click()
time.sleep(1)

text = driver.find_element(By.XPATH,'//legend[text()="Radio Button Example"]').text
print(text)

driver.quit()