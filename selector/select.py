from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

dropdown = Select(driver.find_element(By.ID,'dropdown-class-example'))

dropdown.select_by_visible_text('Option1')
time.sleep(2)

dropdown.select_by_index(2)
time.sleep(2)

dropdown.select_by_value('option3')
time.sleep(2)