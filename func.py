import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import func
from selenium.common.exceptions import NoSuchElementException
import re
import random

def login (username, password, driver):
    #accept cookie button has been pressed
    cookie  = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    cookie.send_keys(Keys.RETURN)

    #username and password details have been entered
    time.sleep(5)
    user = driver.find_element_by_name("username")
    pwb = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    user.clear()
    user.send_keys(username)
    pwb.clear()
    pwb.send_keys(password)
    submit.send_keys(Keys.RETURN)
    time.sleep(3)