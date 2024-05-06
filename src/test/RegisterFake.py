class RegisterFake:
    def __init__(self):
        self.registered_users = []

    def register(self):
        self.registered_users.append(("hello@world.com", "Firstname", "Lastname", "password"))
        print("Signed up successfully!")
