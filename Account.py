import requests

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
            return False
        return True

    def add_name_to_file(self):
        with open('first.csv', 'rb') as inp, open('first_edit.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[2] != "0":
                writer.writerow(row)