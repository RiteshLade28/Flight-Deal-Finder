import requests

class User_Details:
    def __init__(self):
        self.SHEETY_USERS_ENDPOINT = "https://api.sheety.co/e629599160fc8fdcc5c5e66da4b778ae/flightDeals/users"
        print("Welcome to Ritesh's Flight Club")
        print("We find best flight deals and email you")
        self.first_name = input("What is your First Name?")
        self.last_name = input("What is yout Last Name?")
        self.email = input("What is your email?")
        self.confirm_email = input("Type your email again.")

    def add_user(self):
        if self.email == self.confirm_email:
            new_user = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.email,
                }
            }
            response = requests.post(url=self.SHEETY_USERS_ENDPOINT, json=new_user)
            # print(response.text)
            print("You are in the club!")
        else:
            print("Please check you mail")





