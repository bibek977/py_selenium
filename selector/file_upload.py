from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://the-internet.herokuapp.com/upload"
driver.get(url)
time.sleep(2)

driver.find_element(By.ID,'file-upload').send_keys('/home/bibek/Webcam/2022-09-27-215443.jpg')
time.sleep(4)

driver.find_element(By.ID,'file-submit').click()
time.sleep(2)

driver.quit()