import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get('https://www.google.com/') #opens up google
search = driver.find_element_by_name('q') # the name of the searchbox
search.send_keys('mammootty',Keys.ENTER)


elem = driver.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()

value = 0
for i in range(30):  #Scrolls the page 50 times
 driver.execute_script('scrollBy("+ str(value) +",+100);')
 value += 100
 time.sleep(4)


elements = driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')
try:
    os.mkdir('dataset_image/mammootty')
except FileExistsError:
    pass


count = 0
for i in elements:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('dataset_image/mammootty', 'image' + str(count) + '.jpg'))
            if count%10 == 0: print("downloaded",count,"images")
        else:
            raise TypeError
    except TypeError:
        pass