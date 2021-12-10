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
#importing classes from other python folders
from Account import Account
from Posts import Post
from MyAccount import Myaccount
from Menu import Menu


class Simulation:
    def __init__(self):
        """Run Insta Account Simulation"""
        self.SimTitle = datetime.datetime.now().strftime("%d-%b-%Y-%H%M")
        pass

    def run (self):
        #check the validity
        #if invalid, place name in invalid csv
        #if account is valid, put names in working csv
        #get names from csv
        #make them into accounts 
        #append those account into an array 
        pass
        

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

    def create_account_array(self, usernames):
        account_array = []
        for username in usernames:
            user = Account(username)
            if user.check_validity():
                account_array.append(user)
            else:
                
        return account_array






def Main():
    execute = Simulation()
    execute.run()

if __name__ == "__main__": 
    Main()



