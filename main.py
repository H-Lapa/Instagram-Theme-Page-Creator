# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#time related imports
import time
import datetime
#math import
import random
#file control import
import os
#request imports
import urllib
import urllib.request
# to be abe to read csv files
import csv

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

    def check_validity(self):
        response = requests.get(self.link)
        if response.status_code == 404 :
            #If the account doesn't exist
            #delete name from csv 
            # move to invalid csv
            pass

 

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

    def log_out(self):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit code \n     4.Resume \n    5.Login"

class Simulation:
    def __init__(self):
        """Run Insta Account Simulation"""
        pass

    def run (self):
        #get names from csv, put then into an accounts array
        array =self.get_usernames()
        self.folder_structure(array)

    def get_usernames (self):
        """ Produces arary with Usernames from CSV"""

        #Opens the file
        file = open('Usernames.csv')
        type(file)

        #reads items from rows
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
                rows.append(row)

        #closes the files
        file.close()
        return rows

    def folder_structure(self, usernameArray):

        #creates the parent file for the simulation 
        folder_title = datetime.datetime.now()
        folder_title_str = folder_title.strftime("%d-%b-%Y-%H%M")
        os.makedirs(folder_title_str, exist_ok = True)

        #creates account files
        for username in usernameArray:
            path = os.path.join(folder_title_str, str(username[0]))
            os.makedirs(path, exist_ok = True)




def Main():
    execute = Simulation()
    execute.run()

if __name__ == "__main__": 
    Main()



