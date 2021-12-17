from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Myaccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login (self, driver):
        driver.get("https://www.instagram.com/")
        #accept cookie button has been pressed
        try:
            cookie = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
            cookie.send_keys(Keys.RETURN)
        except:
            pass

        #username and password details have been entered
        time.sleep(5)
        user = driver.find_element_by_name("username")
        pwb = driver.find_element_by_name("password")
        user.clear()
        user.send_keys(self.username)
        pwb.clear()
        pwb.send_keys(self.password)
        submit = driver.find_element_by_class_name("L3NKy")
        time.sleep(2)
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

        #check if details worked

        #This finds the error message and uses 'elements' to store elements in array but there should only be one
        check = driver.find_elements_by_id("slfErrorAlert") 
        
        #checks if the error element is there and acts on it
        if check == []:
            print("success")
        else:
            print("Details are incorrect!")
            driver.close()

    def logout(self):
        pass

    def uploadPost(self):
        pass