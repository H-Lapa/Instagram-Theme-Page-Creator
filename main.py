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

    def run (self):
        #check the validity
        #if invalid, place name in invalid csv
        #if account is valid, put names in working csv
        #get names from csv
        #make them into accounts 
        #append those account into an array 


        # list = self.get_usernames()
        driver = webdriver.Firefox(executable_path=r'C:\Users\tuxo9\Downloads\geckodriver\geckodriver.exe')
        acc = Myaccount("sou.ohugo", "Paracetamol12")
        acc.login(driver)
        # self.account_array = self.create_account_array(list, driver)
        #self.set_intial_dates()

        driver.get("https://www.instagram.com/bot_goose/")
        time.sleep(5)
        end = False
        #loop through elements in first row
        row = 1
        while (end):
            path_part_1 = f"/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[{row}]"

            try:
                for element_in_array in range(1, 4):
                    path = path_part_1 + f"/div[ {element_in_array} ]/a/div/div[1]/img"
                    var = driver.find_element_by_xpath(path).get_attribute("src")
                    print(var)
                    path.send_keys(Keys.RETURN)
                    time.sleep(2)
                    variabletime = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/a/time").get_attribute("datetime")
                    print(variabletime)
                    #find image date 
                    #compare the date
                    #if date is before or the same as latest date
                    #set end to true
                row += 1
            except:
                #scroll down element not found
                pass

        path_part_1 = f"/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[{row}]"
        for element_in_array in range(1, 4):
                path = path_part_1 + f"/div[ {element_in_array} ]/a/div/div[1]/img"
                var = driver.find_element_by_xpath(path)
                print(var.get_attribute("src"))

                #new is the element to be clicked to open the image
                new = driver.find_element_by_xpath( path_part_1 + f"/div[{element_in_array}]/a")
                new.send_keys(Keys.RETURN)

                #finds the exit button 
                exitbutton = driver.find_element_by_css_selector(".BI4qX > button:nth-child(1)")
                time.sleep(3)

                #gets the datetime from the element to late be converted to datetime object
                variabletime = driver.find_element_by_css_selector("._1o9PC").get_attribute("datetime")
                exitbutton.send_keys(Keys.RETURN)
                time.sleep(2)
                #prints datetime to know if ive got it
                print(variabletime)
                #turns the date string into a datetime object
                variabletime = datetime.strptime(variabletime, "%Y-%m-%dT%H:%M:%f.000z")

                if self.datetime == variabletime:
                    #end the loop at this position
                    #increment to last value of loop to end it?
                    pass





        #once account array is made
        #set the most recent post date, to todays date for all acounts
        #so that no posts from the when the simulation starts is posted

        #loop for every hour
        #check for new posts
        #each account should add posts to themselves
        #posts should be downloaded
        #then posted in order
        #then update the latestest post date attribute for accounts, so that later we dont get a repeated post

        
        

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



