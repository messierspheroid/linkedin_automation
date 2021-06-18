from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://linkedin.com")

# ******************Login ****************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("chad.bjornberg@gmail.com")
password.send_keys("*Applepass91*")
time.sleep(2)

submit_button = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

# ******************automate messaging ****************

# driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH")
# time.sleep(2)
#
# all_msg_btns = driver.find_elements_by_tag_name("button")
# message_buttons = [btn for btn in all_msg_btns if btn.text == "Message"]
#
# for i in range(0, len(message_buttons)):
#     driver.execute_script("arguments[0].click();", message_buttons[i]) #this is JS bc linkedin is trying to be cute
#     time.sleep(2)
#     main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container']")
#     driver.execute_script("arguments[0].click();", main_div)
#
#     paragraphs = driver.find_elements_by_tag_name("p")
#     paragraphs[-8].send_keys("testing")
#
#     # submit = driver.find_element_by_xpath("//button[@type='submit']").click()
#     # time.sleep(2)
#     # close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
#     # driver.execute_script("arguments[0].click();", close_button)
#     # time.sleep(2)
#
# # print(paragraphs[-2].text)
#
# # *****************add contacts ***************
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH")
time.sleep(2)

all_contact_btns = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_contact_btns if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)

    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)

    close = send = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)
