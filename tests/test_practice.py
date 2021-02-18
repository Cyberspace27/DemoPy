from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

exec_path_chrome  =  r"C:\chromedriver.exe"
URL = r"https://www.wikipedia.org/"
en_locator_link = "js-link-box-en"
search_locator = "searchInput"
search_text = "New York city"

wait_time_out = 15

driver = webdriver.Chrome(exec_path_chrome)

wait = W(driver, wait_time_out)

driver.get(URL)
driver.maximize_window()
#en_locator_link = wait.until(E.presence_of_element_located(By.ID, en_locator_link))
en_locator_link = driver.find_element(By.ID, en_locator_link)

driver.implicitly_wait(5)

en_locator_link.click()
input_box_element = driver.find_element(By.ID, search_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()
driver.quit()
