
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

s = Service("./chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("http://www.tutorialsninja.com/demo/")

driver.minimize_window()

try:
    wait = WebDriverWait(driver, 5)
    search_field = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    search_field.clear()
    search_field.send_keys("iphone")
    search_field.send_keys(Keys.RETURN)

except:
    print("No clickable!")

WebDriverWait(driver, timeout=5)
button_field = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
if button_field.is_enabled():
    button_field.click()
else:
    print("unclickable!")

try:
    my_object = WebDriverWait(driver, timeout=5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'fa-shopping-cart'))
    )
    item_field = driver.find_element(By.CLASS_NAME, "fa-shopping-cart")
    item_field.click()
except:
    print('Object is probably null')
else:
    if item_field is not None:
        print(item_field)
finally:
    pass

checkout_field = driver.find_element(By.CLASS_NAME, 'fa-share')
checkout_field.click()

quantity_field = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
quantity_field.clear()
quantity_field.send_keys(5)
quantity_field.send_keys(Keys.RETURN)

con_link = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/a')
con_link.click()

mac_field = driver.find_element(By.CLASS_NAME, 'image')
mac_field. click()

textbox_field = driver.find_element(By.NAME, 'quantity')
textbox_field.click()

add_to_button = driver.find_element(By.ID, 'button-cart')
add_to_button.click()

go_to_card_elem = driver.find_element(By.CLASS_NAME, "fa-shopping-cart")
go_to_card_elem.click()


def my_res(total_1):     #total = [123.20, 122, 4, 40.20,]
    sum = 0                      # Sum = sum(total)
    for i in total_1:            # print(Sum)
        sum += i
    return sum


s1 = driver.find_element(By.CSS_SELECTOR, '#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(5)').text
print(s1[1:])
s_1 = float(s1[1:])
print(s_1)

s2 = driver.find_element(By.CSS_SELECTOR, '#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(5)').text
print(s2[1:])
s_2 = float(s2[1:])
print(s_2)

total = [s_1, s_2]
res = my_res(total)
print(res)

q_textbox = driver.find_element(By.CSS_SELECTOR, '#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > input').text

q_textbox_2 = driver.find_element(By.CSS_SELECTOR, '#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > input').text

sum = 0
for i in q_textbox and q_textbox_2:
    sum += i

print(q_textbox and q_textbox_2)



con_field = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/a')
con_field.click()

acc_field = driver.find_element(By.CLASS_NAME, 'fa-user')
acc_field.click()

log_link = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
log_link.click()

rc_field = driver.find_element(By.ID, 'input-email')
rc_field.click()
rc_field.send_keys('adam_johnson@gmail.com')
rc_field.send_keys(Keys.RETURN)

pswd_field = driver.find_element(By.NAME, 'password')
pswd_field.click()
pswd_field.send_keys('random_password!')
pswd_field.send_keys(Keys.RETURN)

log_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
log_button.click()

driver.close()

