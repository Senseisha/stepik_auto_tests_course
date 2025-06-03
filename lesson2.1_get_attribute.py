from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.TAG_NAME, "img")
  x = x_element.get_attribute("valuex")


  # x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
  # x = x_element
  y = calc(x)


  form = browser.find_element(By.ID, "answer")
  form.send_keys(y)

  option1 = browser.find_element(By.ID, "robotCheckbox")
  option1.click()

  option2 = browser.find_element(By.ID, "robotsRule")
  option2.click()

  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()

finally:
  time.sleep(10)
  browser.quit()


