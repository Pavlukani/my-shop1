##### Регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# 1
driver.get('https://practice.automationtesting.in')
# 2
account=driver.find_element_by_link_text("My Account").click()
# 3
email=driver.find_element_by_id("reg_email")
email.send_keys('be-tester@mail.ru')
# 4
password=driver.find_element_by_id("reg_password")
password.send_keys('Be-tester12345')
# 5
register=driver.find_element_by_css_selector('[name="register"]').click()


########### Логин в систему
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# 1
driver.get('https://practice.automationtesting.in')
# 2
account=driver.find_element_by_link_text("My Account").click()
# 3
email=driver.find_element_by_id("username")
email.send_keys('be-tester@mail.ru')
# 4
password2=driver.find_element_by_id("password")
password2.send_keys('Be-tester12345')
# 5
login=driver.find_element_by_css_selector('[name="login"]').click()
# 6
logout=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
