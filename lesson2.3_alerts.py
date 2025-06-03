from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    form = browser.find_element(By.ID, "answer")
    form.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
   time.sleep(10)
   browser.quit()


