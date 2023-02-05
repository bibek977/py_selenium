from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

checkboxes = driver.find_elements(By.XPATH,"//input[starts-with(@id,'checkBox')]")

for checkbox in checkboxes:
    if checkbox == checkboxes[1]:
        pass
    else:
        checkbox.click()
