class RegisterStub:
    def __init__(self):
        self.registered_users = []

    def register(self, email_address, first_name, last_name, password):
        self.registered_users.append((email_address, first_name, last_name, password))

