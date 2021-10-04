import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import func
import json

#setting up and loading the browser
#driver = webdriver.Firefox(executable_path=r'C:\Users\tuxo9\Downloads\geckodriver\geckodriver.exe')
#driver.get("https://www.instagram.com/")

#log in
#username = "enter username"
#password = "enter password"
#func.login(username, password, driver)

#get names of profiles from CSV file, each having a corresponding date
# if date empty add, most recent post date
#downlaod all the images and upload them
# else if there is a date
# check the most recent date
# if the date is equal, move onto the next profile
# else check all the posts until you reach the post with the same date
#download and upload all the new posts

func.createFolders(func.setUp())
