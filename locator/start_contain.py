from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

table = driver.find_element(By.XPATH,"//table[starts-with(@id,'pro') and contains(@name,'our')]")

print(table.find_element(By.XPATH,'//tbody/tr[2]/td[1]').text)

