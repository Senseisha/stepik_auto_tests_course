from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_1.send_keys('Ivan')
    input_2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_2.send_keys('Petrov')
    input_3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_3.send_keys('VAnya@ya.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'selenium_python.txt')
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    


    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()




