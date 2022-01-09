class Post:
    def __init__(self, link, date):
        self.link = link
        self.date = date # can use datetime liabry
        self.caption = ""

    def download(self, name):
        self.name = name
        urllib.request.urlretrieve(self.link, "Images/" + name +"/" + currentdateandtimeposted + ".png")

    def upload_post(self, driver, simTitle):
        # go to the upload section of instagram
        driver.get("https://www.instagram.com/create/select/")

        #upload the image by selecting the file
        driver.find_element_by_class_name("sqdOP  L3NKy   y3zKF     ").send_keys(os.getcwd()+"/" + simTitle + "/" + self.name + ".png")

        #submit the file location
        driver.find_element_by_id("submit").click()

        #click the nect button
        next = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
        next.send_keys(Keys.RETURN)

        # click the next button again
        next.send_keys(Keys.RETURN)

        # next button has become share but is in same location
        next.send_keys(Keys.RETURN) # now the post has been shared