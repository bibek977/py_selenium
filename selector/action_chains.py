from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = "https://rahulshettyacademy.com/AutomationPractice/"
url = "https://the-internet.herokuapp.com/context_menu"
driver.get(url)

action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
# time.sleep(2)
# action.move_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'Top')]")).click().perform()

action.context_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()
action.double_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()

time.sleep(2)
driver.quit()