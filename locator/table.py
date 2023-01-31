from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

table = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]")
print(table.text)

time.sleep(2)

driver.quit()