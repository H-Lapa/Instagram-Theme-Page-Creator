import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from Posts import Post

class Account:
    def __init__(self, username):
        self.username = username
        self.link = "https://www.instagram.com/" + username + "/"
        self.posts_array = []
        self.latest_post_date = ''

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

    def set_date(self, date):
        self.latest_post_date = date
        return

    def fetch_posts(self, driver):
        driver.get(self.link)
        time.sleep(5)
        end = False
        row = 1
        array = []
        while (end == False):
            intial_path = f"/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[{row}]"

            try:
                for element_in_row in range(1, 4):
                    #gets the image url, which can be used to download later
                    path = intial_path + f"/div[{element_in_row}]/a/div/div[1]/img"
                    var = driver.find_element_by_xpath(path).get_attribute("src")
                    print(var)

                    #Element to be clicked to open the image to full width
                    image_button = driver.find_element_by_xpath(intial_path + f"/div[{element_in_row}]/a")
                    image_button.send_keys(Keys.RETURN)

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
                    

                    if self.latest_post_date == variabletime:
                        #end the for loop at this position
                        #increment to last value of loop to end it?
                        end = True
                        break
                        #also end the while loop setting end to true
                    else:
                        array.append(Post(var, variabletime))
                        
    
            except NoSuchElementException:
                #scroll down element not found
                driver.execute_script("window.scrollTo(0, 1080)") 

            row += 1

                
        self.set_date(self.array[0].date)
        return array

        #go through the posts until 
        #one has a date before or equal to the date time of latest date post

        #from the post extract:
        #date
        #link
        #the caption

        #append posts which are before to the latest date post
        #once all have been added to the array
        #set the latest date post to the date of the post in 0 index
        
                


