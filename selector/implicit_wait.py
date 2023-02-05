from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://chercher.tech/practice/implicit-wait-example"
driver.get(url)

driver.implicitly_wait(30)

c_1 = driver.find_element(By.XPATH,'//div[@id="q"]/input[1]')
c_1.click()
c_3 = driver.find_element(By.XPATH,'//div[@id="q"]/input[3]').click()
 
time.sleep(2)
driver.quit()