import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

    def check_validity(self, driver):
            driver.get(self.link) 
            time.sleep(5)
            variable = driver.find_element_by_tag_name("h2")
            if variable.text == "Sorry, this page isn't available.":
                return False
            else:
                return True

    def add_name_to_file(self, filename, csvname):
        path = filename + '/'+ csvname +'.csv'
        with open(path,'a') as fd:
            fd.write(self.username)

    def remove(self):
        #removes line from txt file
        lines = list()
        with open('Usernames.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == self.username:
                        lines.remove(row)
        #writes back to the file without txt row
        with open('Usernames.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

                