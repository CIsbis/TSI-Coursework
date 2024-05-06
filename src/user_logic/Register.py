import os
import csv

class Register:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def register(self):
        self.email_address = input("Enter your email address: ")
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.password = input("Enter password: ")

        current_dir = os.getcwd()

        while current_dir and not current_dir.endswith("TSI-Coursework"):
            current_dir = os.path.dirname(current_dir)

        if current_dir.endswith("TSI-Coursework"):
            resource_dir = os.path.join(current_dir, "src", "resource")
        else:
            print("Project folder not found.")
            return

        if not os.path.exists(resource_dir):
            print("Resource directory does not exist.")
            return

        try:
            with open(os.path.join(resource_dir, self.csv_file), 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.email_address, self.first_name, self.last_name, self.password])
                print("Signed up successfully!")
        except Exception as e:
            print("An error occurred while writing to the file:", e)

if __name__ == "__main__":
    Register("customer.csv").register()
