from selenium import webdriver 
import pyttsx3 as p #pip install pyttsx3
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path = 'C:\Web Drivers\chromedriver.exe') #here we have to specify the path of chrome webdriver of your own PC after downloading it.
driver.get(url = "http://gmail.com/")
login_id = driver.find_element_by_xpath('//*[@id="identifierId"]')

login_id.send_keys('Your_email id')
login_click = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
login_click.click()
time.sleep(5)
password_enter = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

password_enter.send_keys('Your_password')
password_click = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
password_click.click()
time.sleep(20)
compose_email = driver.find_element_by_xpath('//*[@id=":3o"]/div/div')
compose_email.click()
time.sleep(10)
to_address = driver.find_element_by_xpath('//*[@id=":99"]')
to_address.send_keys('Email id of the person whom you want to send')
input_subject = driver.find_element_by_xpath('//*[@id=":8r"]')
input_subject.send_keys('Hola')
email_content = driver.find_element_by_xpath('//*[@id=":9w"]')
email_content.send_keys('Testing')
time.sleep(5)
sendElem = driver.find_element_by_id(":8h")
sendElem.click()
import pyttsx3 as p
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path = 'C:\Web Drivers\chromedriver.exe')
driver.get(url = "http://gmail.com/")
login_id = driver.find_element_by_xpath('//*[@id="identifierId"]')
login_id.clear()
login_id.send_keys('Your_email id')
login_click = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
login_click.click()
time.sleep(5)
password_enter = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_enter.clear()
password_enter.send_keys('Your_password')
password_click = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
password_click.click()
time.sleep(20)
compose_email = driver.find_element_by_xpath('//*[@id=":3o"]/div/div')
compose_email.click()
time.sleep(10)
to_address = driver.find_element_by_xpath('//*[@id=":99"]')
to_address.send_keys('Email id of the person whom you want to send')
input_subject = driver.find_element_by_xpath('//*[@id=":8r"]')
input_subject.send_keys('Hola')
email_content = driver.find_element_by_xpath('//*[@id=":9w"]')
email_content.send_keys('Testing')
time.sleep(5)
sendElem = driver.find_element_by_id(":8h")
sendElem.click()
