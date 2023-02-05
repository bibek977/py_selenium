from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

name = driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Bibek")
confirm = driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()

# driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
time.sleep(3)

popup = driver.switch_to.alert
assert 'Bibek' in popup.text
popup.accept()
time.sleep(3)

driver.quit()