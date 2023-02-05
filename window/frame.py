from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']"))

driver.find_element(By.XPATH,"//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='consulting'][normalize-space()='Job Support']").click()

driver.switch_to.default_content()

time.sleep(4)
driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']").click()
time.sleep(4)