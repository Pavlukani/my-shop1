import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
from selenium.webdriver.common.by import By
# 1
driver.get('https://practice.automationtesting.in')
# 2
driver.execute_script("window.scrollBy(0, 600);")
# 3
read_more_btn=driver.find_element_by_css_selector('[data-product_id="160"]').click()
# 4
reviews=driver.find_element_by_class_name("reviews_tab").click()
# 5
stars=driver.find_element_by_class_name('star-5').click()
# 6
comment=driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
# 7
name=driver.find_element_by_id("author")
name.send_keys("Jonh")
# 8
mail=driver.find_element_by_id('email')
mail.send_keys("Be-tester@mail.ru")
# 9
submit=driver.find_element_by_class_name("submit").click()
