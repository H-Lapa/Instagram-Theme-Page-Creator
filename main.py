# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import func
# import json
#import datetime

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
class Myaccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass

    def uploadPost(self):
        pass


class Account:
    def __init__(self, username):
        self.username = username
        self.link = "https://www.instagram.com/" + username + "/"
        self.posts_array = []

    def get_posts (self):
        return self.posts_array

    def append (self, post):
        self.posts_array.append(post)

    def create_folder(self):
        directory = self.username
        path = os.path.join("Images", directory)
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)
 

class Post:
    def __init__(self, link, date):
        self.link = link
        self.date = date # can use datetime liabry
        self.caption = ""

    def download(self, name):
        urllib.request.urlretrieve(self.link, "Images/" + name +"/" + currentdateandtimeposted + ".png")


class Menu:
    def __init__(self):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit code \n     4.Resume \n    5.Login"

    def logged_in(self, username):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit code \n     4.Resume \n    Logged in as" + username



class Simulation:
    def __init__(self):
        """Run Insta Account Simulation"""
        pass

    def run (self):
        pass









