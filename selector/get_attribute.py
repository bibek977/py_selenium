from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

text = driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']").text
print(text)

placeholder = driver.find_element(By.XPATH,"//input[@id='name']").get_attribute('placeholder')
print(placeholder)

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Bibek Bhattarai")

data = driver.find_element(By.XPATH,"//input[@id='name']").get_attribute('value')
print(data)

time.sleep(2)
driver.quit()