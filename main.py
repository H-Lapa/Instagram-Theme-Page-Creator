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



