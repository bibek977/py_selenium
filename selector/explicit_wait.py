from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = "https://chercher.tech/practice/implicit-wait-example"
url = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
driver.get(url)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="q"]/input[1]')))
# driver.find_element(By.XPATH,'//div[@id="q"]/input[1]').click()
driver.find_element(By.XPATH,"//button[@id='populate-text']").click()
WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH,"//h2[@id='h2']"), 'Selenium Webdriver'))
print(driver.find_element(By.XPATH,"//h2[@id='h2']").text)

time.sleep(2)
driver.quit()