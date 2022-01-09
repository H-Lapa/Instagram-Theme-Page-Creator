# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#time related imports
import time
import datetime
from datetime import datetime
#math import
import random
#file control import
import os
#request imports
import urllib
import urllib.request
import requests
# to be abe to read csv files
import csv
#importing classes from other python folders
from Account import Account
from Posts import Post
from MyAccount import Myaccount
from Menu import Menu


class Simulation:
    def __init__(self):
        """Run Insta Account Simulation instance"""
        self.datetime = datetime.now()
        self.SimTitle = self.datetime.strftime("%d-%b-%Y-%H%M")
        self.account_array = []
        self.post_queue = []

    def run (self):
        #check the validity
        #if invalid, place name in invalid csv
        #if account is valid, put names in working csv
        #get names from csv
        #make them into accounts 
        #append those account into an array 
        driver = webdriver.Firefox(executable_path=r'C:\Users\tuxo9\Downloads\geckodriver\geckodriver.exe')

        menu = Menu()
        arr = self.get_usernames()
        self.folder_structure(arr)
        self.account_array = self.create_account_array(arr, driver)
        self.set_intial_dates()

        while True:

            for account in self.account_array:
                account.fetch_posts(driver)

            self.post_queue_generator()

        #loop for every hour
        #check for new posts
        #each account should add posts to themselves
        #posts should be downloaded
        #then posted in order
        #then update the latestest post date attribute for accounts, so that later we dont get a repeated post

        if self.post_queue > 6:
            length = 6
        else:
            length = self.post_queue
        
        #3600 is the second in an hour
        interval = 3600/length
        for x in range(length):
            time.sleep(interval)
            self.post_queue[self.post_queue.length - 1].upload_post(driver, self.SimTitle)
            self.post_queue.pop()


        
    def post_queue_appender (self):

        #finding out how many posts there are
        total_posts = 0
        for x in self.account_array:
            total_posts += len(x.posts_array)
            
        #loops until all posts are added to the post_queue
        while len(self.post_queue) != total_posts:
            oldest_post = self.account_array[0].posts_array[len(posts_array)-1]
            smallest_time = oldest_post.date
            for i in range(1, len(self.account_array)):
                new_post = self.account_array[i].posts_array[len(posts_array)-1]
                if smallest_time > new_post.date:
                    smallest_time = new_post.date
                    oldest_post = new_post

            oldest_post.pop()
            self.post_queue.append(oldest_post)

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

        #creates the parent file for the simulation using the name
        os.makedirs(self.SimTitle, exist_ok = True)

        #creates account files
        for username in usernameArray:
            path = os.path.join(self.SimTitle, str(username[0]))
            os.makedirs(path, exist_ok = True)

    def create_account_array(self, usernames, driver):
        """Returns array with valid users"""
        account_array = []
        for x in range(len(account_array)):
            user = Account(usernames[x][0])
            print(user.username)
            if user.check_validity(driver) == True:
                print("True")
                account_array.append(user)
            else:
                print("False")
                user.add_name_to_file(self.SimTitle, "Invalid")
                user.remove()

        return account_array

    def set_intial_dates(self):
        for account in self.account_array:
            account.set_date(self.datetime)
        return


def Main():
    execute = Simulation()
    execute.run()

if __name__ == "__main__": 
    Main()



