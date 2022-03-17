import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium


# initialize driver


def login(username_, password_):
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(30)

    # accepting the cookies
    try:
        cookies_accept= driver.find_element_by_xpath('//button[text()="Accept"]')
        cookies_accept.click()
        time.sleep(1)
    except:
        pass

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    username.click()
    username.send_keys('_gautambisht_11')
    time.sleep(1)

    password.click()
    password.send_keys('e8c2cadf2148')
    time.sleep(1)

    log_in=driver.find_element_by_xpath('//div[text()="Log In"]')
    log_in.click()
    time.sleep(4)

    # credential storage
    try:
        driver.implicitly_wait(30)
        credentials= driver.find_element_by_xpath('//button[text()="Not Now"]')
        credentials.click()
        time.sleep(1)
    except:
        pass

    #  notifications
    try:
        driver.implicitly_wait(30)
        notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
        notifications.click()
        time.sleep(1)
    except:
        pass

def follow_like_comment():
        driver.implicitly_wait(30)
        search_1 = driver.find_element_by_xpath('//span[text()="Search"]')
        driver.implicitly_wait(30)
        search_1.click()
        time.sleep(1)
        driver.implicitly_wait(30)
        search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
        driver.implicitly_wait(30)
        search_2.send_keys('virat.kohli')
        driver.implicitly_wait(30)
        search_2.send_keys(Keys.ENTER)   
        time.sleep(1)

        count = 0
        while count <2:
            search_2.send_keys(Keys.ENTER)
            count +=1 # count = count +1
            time.sleep(1)
login('testuseraccount24', 'testuser')
follow_like_comment()

while (True):        
        driver.implicitly_wait(30)
        follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
        follow.click()
        time.sleep(10)
        unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button')
        driver.implicitly_wait(30)
        unfollow1.click()
        unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
        driver.implicitly_wait(30)
        unfollow2.click()
        time.sleep(5)
