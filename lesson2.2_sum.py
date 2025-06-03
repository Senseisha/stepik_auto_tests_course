from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
  link = "https://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)

  num1 = browser.find_element(By.XPATH, "//span[@id='num1']")
  x = num1.text
  num2 = browser.find_element(By.XPATH, "//span[@id='num2']")
  y = num2.text
  sum = int(x) + int(y)

  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(value=str(sum))

  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()

finally:
  time.sleep(5)
  browser.quit()



