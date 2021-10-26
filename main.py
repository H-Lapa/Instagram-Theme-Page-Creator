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

#func.createFolders(func.setUp())
func.download("https://scontent-lcy1-1.cdninstagram.com/v/t51.2885-15/e35/68916344_2241220965977167_2794194787179738506_n.jpg?_nc_ht=scontent-lcy1-1.cdninstagram.com&_nc_cat=107&_nc_ohc=rmaDi9RxqfAAX_rD9Ib&tn=u45cFCRPI0W5qZIz&edm=ACWDqb8BAAAA&ccb=7-4&oh=3a85d71654efc9be7b1d9ca564405d83&oe=61800173&_nc_sid=1527a3&ig_cache_key=MjEyMjQ4Nzc0MTI2MzM0MjQ1NQ%3D%3D.2-ccb7-4", "bot_goose", "9OfMay")
