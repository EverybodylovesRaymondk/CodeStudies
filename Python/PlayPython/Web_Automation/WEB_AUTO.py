from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import pandas as pd
from datetime import datetime as dt
import time

#Importing elements and paths
elements = pd.DataFrame(pd.read_excel('ELEMENTS.XLSX'))

#Creating output file
f = open("OUTPUT.TXT","a+")

#Declaring username and password
username = 'raymondk'
password = 'dqo39imf'
url = 'http://ke-ntsa-mas.spsi.co.za/BOMUI/#!/'

#Creating the Chrome driver
driver = webdriver.Chrome(executable_path="C:\\Users\\raymondk\\Downloads\\chromedriver.exe")

#Login Test
f.write(str(dt.now()) +'\tlogin Started'+ '\n')
driver.get(url)
driver.maximize_window()


username_textbox = driver.find_element_by_id(elements['PATH'][0])
username_textbox.send_keys(username)

password_textbox= driver.find_element_by_id(elements['PATH'][1])
password_textbox.send_keys(password)

login_button = driver.find_element_by_css_selector(elements['PATH'][2])
login_button.click()
f.write(str(dt.now()) +'\tlogin completed'+ '\n')

time.sleep(2)
Agency_dropdown = driver.find_element_by_css_selector(elements['PATH'][3])
Agency_dropdown.click()

#Navigate to agency
Agency_search = driver.find_element_by_class_name(elements['PATH'][4])
Agency_search.send_keys('NTSA')
enter = keys.ENTER
Agency_search.send_keys(enter)

f.write(str(dt.now()) +'\tNTSA Navigation Complete'+ '\n')

#navigate to activity
Activity_filter = driver.find_element_by_css_selector(elements['PATH'][5])
Activity_filter.click()
Activity_filter.send_keys('maintainSign')

f.write(str(dt.now()) +'\tActivity Searched'+ '\n')

f.write(str(dt.now()) +' \t'+ driver.title + ' Test Successfull'+ '\n')
f.close()
time.sleep(3)
driver.save_screenshot('Login_image1.png')
driver.close()