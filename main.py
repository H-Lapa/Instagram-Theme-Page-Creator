import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import random
import os
import json
import urllib
import urllib.request

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


def Main():
    execute = Simulation()
    execute.run()

if __name__ == "__main__": 
    Main()



