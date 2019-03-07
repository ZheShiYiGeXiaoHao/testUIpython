#coding = utf-8


import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#google浏览器
capabilities = DesiredCapabilities.CHROME


driver = webdriver.Remote(command_executor="http://172.17.0.1:5001/wd/hub",  desired_capabilities=capabilities )


driver.get("http://172.17.0.1:8999/")



time.sleep(5)
driver.quit()
