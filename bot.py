
                 
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
def getRandomTime1():
        randTime = randint(3, 5)
        return randTime
def getRandomTime2():
        randTime = randint(1180,1190)
        return randTime
def getrandomname():
         randTime = ['viratkohli', 'narendramodi', 'cristiano', 'instagram',  'selenagomez']
         a = random.choice(randTime)
         return a
def login():
        driver.implicitly_wait(30)
        a12 = driver.get("https://instagram.com/")    
        driver.implicitly_wait(30)        
        time.sleep(getRandomTime())
        a = driver.find_element_by_xpath('''//*[@id="loginForm"]/div/div[1]/div/label/input''')
        a.send_keys('YOUR-USERNAME')
        time.sleep(getRandomTime1())
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('YOUR-PASSWORD')
        time.sleep(getRandomTime1())     
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('Succesfully logined')

        time.sleep(60)
        


        
        return
def follow1():
    driver.refresh()
    time.sleep(4)
    driver.get(f"https://instagram.com/{getrandomname()}")
    time.sleep(10)
    driver.implicitly_wait(30)
    try: 
       driver.implicitly_wait(30)
       time.sleep(getRandomTime1())
       follow=driver.find_element_by_xpath("//*[text()='Follow']")
       time.sleep(getRandomTime1())
       follow.click()
       driver.refresh()
       time.sleeep(20)
    except:
          driver.implicitly_wait(30)
          button = driver.find_element_by_xpath("//button[@class='_abn9 _abnd _abni _abnn']")
          button.click()
          time.sleep(getRandomTime1())
          driver.find_element_by_xpath("//*[text()='Unfollow']").click()
          time.sleep(getRandomTime())
          driver.refresh()

    driver.implicitly_wait(30)
    button = driver.find_element_by_xpath("//button[@class='_abn9 _abnd _abni _abnn']")
    button.click()
    time.sleep(getRandomTime1())
    driver.find_element_by_xpath("//*[text()='Unfollow']").click()
    time.sleep(getRandomTime())
    


    
login()
 
while True:

    follow1()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    follow()
    
    
    time.sleep(81005)
    
