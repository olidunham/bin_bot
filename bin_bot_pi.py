# import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import dateutil.parser as dparser

# intial url
url = 'https://bmsdchosting.net/waste-services/mid-suffolk-bin-collection/'

chromedriver_location = "/lib/chromium-browser/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get(url)

enter_address_xpath = '//*[@id="txt_street"]'
search_button_xpath = '//*[@id="but_submit"]'
next_bin_xpath = '/html/body/ul/li[1]'
next_next_bin_xpath = '/html/body/ul/li[2]'      

driver.find_element(By.XPATH, enter_address_xpath).send_keys('11 Brick Drive')
driver.find_element(By.XPATH, search_button_xpath).click()


driver.implicitly_wait(30)

next_bin = driver.find_element(By.XPATH, next_bin_xpath).text
next_next_bin = driver.find_element(By.XPATH, next_next_bin_xpath).text

print(next_bin)
print(next_next_bin)

driver. close()

next_bin_date = dparser.parse(next_bin,fuzzy=True)

if 'refuse' in next_bin:
    bin_string = 'Black bin tomorrow (' + next_bin_date.strftime("%A %d %B") + ')'
    print(bin_string)
else:
    bin_string = 'Green bin tomorrow (' + next_bin_date.strftime("%A %d %B") + ')'
    print(bin_string)
    
bin_string = bin_string.replace(' ','+')

callbot_api = '379629'
my_no = '+447412851686'

callbot_string ='https://api.callmebot.com/whatsapp.php?phone=' + my_no + '&text=' + bin_string + '&apikey=' + callbot_api
callbot_string

#Send whatsapp message using api
response = requests.get(callbot_string)