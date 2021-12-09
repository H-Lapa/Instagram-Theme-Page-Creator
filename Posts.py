class Post:
    def __init__(self, link, date):
        self.link = link
        self.date = date # can use datetime liabry
        self.caption = ""

    def download(self, name):
        urllib.request.urlretrieve(self.link, "Images/" + name +"/" + currentdateandtimeposted + ".png")