from selenium import webdriver

path_exec_chrome= r"C://chromedriver.exe"
URL = "https://pinatours.000webhostapp.com/"
driver = webdriver.Chrome(path_exec_chrome)
driver.get(URL)
driver.close()