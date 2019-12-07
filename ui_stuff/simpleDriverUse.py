import time
from selenium import webdriver

d = webdriver.Firefox()
d.get("https://www.mtggoldfish.com")
time.sleep(5)
d.close()