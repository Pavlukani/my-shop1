####### Отображение страницы товара
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
email=driver.find_element_by_id("username")
email.send_keys('be-tester@mail.ru')
password2=driver.find_element_by_id("password")
password2.send_keys('Be-tester12345')
login=driver.find_element_by_css_selector('[name="login"]').click()
# 3
shop=driver.find_element_by_link_text("Shop").click()
# 4
book_html=driver.find_element_by_css_selector('[data-product_id="181"]').click()
# 5
html_text = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))


##### Количество товаров в категории
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# 1
driver.get('https://practice.automationtesting.in')
# 2
account=driver.find_element_by_link_text("My Account").click()
email=driver.find_element_by_id("username")
email.send_keys('be-tester@mail.ru')
password2=driver.find_element_by_id("password")
password2.send_keys('Be-tester12345')
login=driver.find_element_by_css_selector('[name="login"]').click()
# 3
shop=driver.find_element_by_link_text("Shop").click()
# 4
html_btn=driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()
# 5
html_count=driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(html_count) == 3:
    print("Отображается три товара")
else:
    print("Ошибка: Отоброжается не три товара")

##### Сортировка товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
# 1
driver.get('https://practice.automationtesting.in')
# 2
account=driver.find_element_by_link_text("My Account").click()
email=driver.find_element_by_id("username")
email.send_keys('be-tester@mail.ru')
password2=driver.find_element_by_id("password")
password2.send_keys('Be-tester12345')
login=driver.find_element_by_css_selector('[name="login"]').click()
# 3
shop=driver.find_element_by_link_text("Shop").click()
# 4
selector= driver.find_element_by_class_name("orderby")
selector_check =selector.get_attribute("value")
if selector_check == "menu_order":
    print("Сортировка по умолчанию")
else:
    print("Ошибка: выбрана не правильная сортировка")
# 5
from selenium.webdriver.support.select import Select
selector=driver.find_element_by_class_name("orderby")
select=Select(selector)
select.select_by_value("price-desc")
# 6
selector = driver.find_element_by_class_name("orderby")
selector_check =selector.get_attribute("value")
if selector_check == "price-desc":
    print("Сортировка от большего к меньшему")
else:
    print("Ошибка: выбрана не правильная сортировка")


######## Отображение, скидка товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# 1
driver.get('https://practice.automationtesting.in')
# 2
account=driver.find_element_by_link_text("My Account").click()
email=driver.find_element_by_id("username")
email.send_keys('be-tester@mail.ru')
password2=driver.find_element_by_id("password")
password2.send_keys('Be-tester12345')
login=driver.find_element_by_css_selector('[name="login"]').click()
# 3
shop=driver.find_element_by_link_text("Shop").click()
# 4
android_book=driver.find_element_by_css_selector("[data-product_id='169']").click()
# 5
book_old_price=driver.find_element_by_css_selector(".price > del > span")
book_old_price_text=book_old_price.text
assert book_old_price_text == "₹600.00"
# 6
book_new_price=driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text=book_new_price.text
assert book_new_price_text == "₹450.00"
# 7
book_cover=WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CLASS_NAME, "images")))
book_cover.click()
# 8
book_cover_close=WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
book_cover_close.click()


##### Проверка цены в корзине
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 1
driver.get('https://practice.automationtesting.in')
# 2
shop=driver.find_element_by_link_text("Shop").click()
# 3
add_book=driver.find_element_by_css_selector("[data-product_id='165']").click()
# 4
count_item=driver.find_element_by_class_name("cartcontents")
count_item_text=count_item.text
assert count_item_text == "1 item"
price_item=driver.find_element_by_css_selector(".wpmenucart-contents .amount")
price_item_text=price_item.text
assert price_item_text == "₹350.00"
# 5
basket=driver.find_element_by_css_selector('[title="View your shopping cart"]').click()
# 6
subtotal= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount"), "₹350.00"))
# 7
total= WebDriverWait(driver, 10).until(
   EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹357.00"))


####### Покупка товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
# 1
driver.get('https://practice.automationtesting.in')
# 2
shop=driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
# 3
add_book=driver.find_element_by_css_selector("[data-product_id='165']").click()
# 4
basket=driver.find_element_by_css_selector('[title="View your shopping cart"]').click()
# 5
proceed_btn=WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
proceed_btn.click()
# 6
first_name=driver.find_element_by_id("billing_first_name")
first_name.send_keys("John")
last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Smith")
email=driver.find_element_by_id("billing_email")
email.send_keys("Be-tester@mail.ru")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("89996543221")
selector=driver.find_element_by_id("select2-chosen-1").click()
field=driver.find_element_by_id("s2id_autogen1_search")
field.send_keys("Russia")
add_country=driver.find_element_by_css_selector(".select2-result-label").click()
address=driver.find_element_by_id("billing_address_1")
address.send_keys("Lenin avenue")
town=driver.find_element_by_id("billing_city")
town.send_keys("Moscow")
state=driver.find_element_by_id("billing_state")
state.send_keys("Moscow")
zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("123456")
# 7
check=driver.find_element_by_id("payment_method_cheque").click()
# 8
order=driver.find_element_by_id("place_order").click()
# 9
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# 10
some_element2= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
