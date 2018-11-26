import time
time.sleep(5)

from selenium import webdriver
driver=webdriver.Chrome("C:\\git\\cavisson\\automation\\sel_jenkins\\chromedriver")
time.sleep(1)
driver.get("http://10.10.30.185")
time.sleep(1)
driver.find_element_by_xpath("/html/body/entry/login/div/div[2]/div/form/div[2]/input").send_keys("aloukik")
time.sleep(1)
driver.find_element_by_xpath("/html/body/entry/login/div/div[2]/div/form/div[3]/input").send_keys("aloukik")
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"login-button\"]").click()
time.sleep(5)

time.sleep(1)
driver.find_element_by_xpath("//i[@class='icon produi-icon-scenario']//parent::span//parent::button").click()
time.sleep(1)
driver.find_element_by_xpath("//span[text()='Scenarios']//parent::a").click()
time.sleep(5)

time.sleep(1)
driver.find_element_by_xpath("variable").click()