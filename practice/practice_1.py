from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.imdb.com/")

movies = driver.find_element(By.CSS_SELECTOR,'.ipc-title__text')
print(movies.text)

fav_list = driver.find_element(By.XPATH,"")
text

driver.quit()