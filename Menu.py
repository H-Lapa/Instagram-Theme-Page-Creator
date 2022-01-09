class Menu:
    def __init__(self):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit program \n     4.Resume \n    5.Login"

    def get_menu(self):
        return self.text

    def get_input(self):
        self.get_menu()
        response = int(input("Input: "))
        return response

    def logged_in(self, username):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit code \n     4.Resume \n    Logged in as" + username

    def log_out(self):
        self.text = "-------------------- \n     1.Execute \n   2.Add Accounts \n    3.Exit code \n     4.Resume \n    5.Login"