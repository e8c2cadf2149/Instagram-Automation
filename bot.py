
                 
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from random import seed
from random import randint
import random


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def getRandomTime():
        randTime = randint(5, 10)
        return randTime  
def getrandomname():
         randTime = ['viratkohli', 'narendramodi', 'cristiano', 'instagram', 'kyliejenner', 'leomessi', 'selenagomez', 'therock']
         a = random.choice(randTime)
         return a
def login():
        driver.implicitly_wait(30)
        driver.get("https://instagram.com")    
        driver.implicitly_wait(30)  
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys('_gautambisht_11')
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('e8c2cadf2147')
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('Succesfully logined')
        return
def follow1():
  x = 0
  while x <10000000000:

    time.sleep(90)
    driver.implicitly_wait(30)
    print('searching')
    b = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    driver.implicitly_wait(30)
    b.send_keys(getrandomname())
    time.sleep(getRandomTime())
    count = 0
    while count <2:
        b.send_keys(Keys.ENTER)
        count +=1 # count = count +1
        time.sleep(getRandomTime())
    try:
       driver.implicitly_wait(30)
       follow = driver.find_element_by_xpath('''//*[@id="mount_0_0_w5"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button''')
       follow.click()
       print('Followed')
       time.sleeep(1210)
    except:
          driver.implicitly_wait(30)
          unfollow1 = driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button''')
          unfollow1.click()
          time.sleep(getRandomTime())
          unfollow2 = driver.find_element_by_xpath('''/html/body/div[6]/div/div/div/div[3]/button[1]''')
          unfollow2.click()
          print('Unfollowed')
          time.sleep(getRandomTime())
    x +=1
login()
while True:    

    follow1()
