from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#PROXY = "10.32.0.1:8080"
startValue = 0

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(r'C:\Users\redas\Downloads\chromedriver_win32\chromedriver.exe')
browser.get('https://www.facebook.com/')

#Login details
#UserName
username_input = browser.find_element_by_xpath('//*[@id="email"]')
username = 'saket96modi@yahoo.com'
username_input.send_keys(username)

#Password
password_input = browser.find_element_by_xpath('//*[@id="pass"]')
passcode = 'random98ds85##'
password_input.send_keys(passcode)

#submit Button
submit_button = browser.find_element_by_xpath('//*[@id="loginbutton"]')
submit_button.click()

#now comes the allow notifications alert
#press escape to remove that
time.sleep(10)
actions = ActionChains(browser)
actions.send_keys(Keys.ESCAPE)
actions.perform()


links = ['https://www.facebook.com/groups/1101742399937747/?ref=bookmarks', 'https://www.facebook.com/groups/161977320940431/']

#Change xrange start value here before every run corresponding to the start no of gen email
for i in range(startValue,len(links)):
    browser.get(links[i])
   
    entire_feed_superset = browser.find_element_by_xpath('//*[@id="pagelet_group_mall"]/div/div/div')
    all_children = entire_feed_superset.find_elements_by_xpath('//*')
    print(all_children)
    print("------")
    #Wait for Documents Required Page to Load
    #CheckPresence   = '//*[@id="undefined-2"]'
    #validCityOption = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, CheckPresence)))
    #time.sleep(3)