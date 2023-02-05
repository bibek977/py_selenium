from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

driver.find_element(By.XPATH,"//a[@id='opentab']").click()
tab = driver.window_handles[1]

driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
window_2 = driver.window_handles[2]

print(driver.window_handles)

driver.switch_to.window(tab)
driver.find_element(By.XPATH,"//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='practice-project'][normalize-space()='Practice']").click()
time.sleep(2)

driver.switch_to.window(window_2)
driver.find_element(By.XPATH,"//a[normalize-space()='Practice']").click()

time.sleep(2)
# driver.quit()