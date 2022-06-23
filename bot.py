
                 
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
         randTime = ['viratkohli', 'narendramodi', 'cristiano', 'instagram', 'leomessi', 'selenagomez', 'therock']
         a = random.choice(randTime)
         return a
def login():
        driver.implicitly_wait(30)
        a12 = driver.get("https://instagram.com/")    
        driver.implicitly_wait(30)        
        time.sleep(getRandomTime())
        a = driver.find_element_by_xpath('''//*[@id="loginForm"]/div/div[1]/div/label/input''')
        a.send_keys('_gautambisht_11')
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('e8c2cadf2147')
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('Succesfully logined')

        time.sleep(6)


        #driver.get(f'''https://www.instagram.com/instagram/''')
        return
def follow1():
 
    driver.get(f"https://instagram.com/{getrandomname()}")
    time.sleep(10)
    driver.implicitly_wait(30)
    try: 
       driver.implicitly_wait(30)
       follow=driver.find_element_by_xpath("//*[text()='Follow']")
       follow.click()
       print('Followed')
       time.sleeep(1210)
    except:
        pass
          # div = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]")
          # button = div.find_elements_by_xpath(".//button")
          # if (button and button[0].text != "Follow"):
          #     if (len(button) > 2):
          #         button[1].click()
          #     else:
          #         button[0].click()
          #         time.sleep(2)
          #         driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()      
    driver.implicitly_wait(30)
    button = driver.find_element_by_xpath("//button[@class='_abn9 _abnd _abni _abnn']")
    button.click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='Unfollow']").click()
    time.sleep(getRandomTime())

login()
while True:    
    
    follow1()
