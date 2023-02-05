from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://www.cleartrip.com/"
driver.get(url)
time.sleep(2)

ad_block = driver.find_element(By.CLASS_NAME,'pb-1').click()
time.sleep(2)

start = driver.find_element(By.XPATH, '//input[@placeholder="Where from?"]').send_keys('sim')
time.sleep(2)

from_to = driver.find_elements(By.XPATH,'//ul[@class="airportList"]/li/div/div/p')
for i in from_to:
    if i.text == 'Simara, NP - Simara (SIF)':
        i.click()
    else:
        pass

time.sleep(2)

end = driver.find_element(By.XPATH,'//input[@placeholder = "Where to?"]').send_keys('kat')
time.sleep(2)

go_to = driver.find_elements(By.XPATH,'//ul[@class="airportList"]/li/div/div/p')

for i in go_to:
    if i.text == 'Kathmandu, NP - Tribuvan (KTM)':
        i.click()
    else:
        pass
time.sleep(2)

driver.quit()