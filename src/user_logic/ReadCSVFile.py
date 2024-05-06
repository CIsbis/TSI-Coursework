import csv
import os

class ReadCSVFile:

    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" not in current_working_directory:
            os.chdir("../../")
            current_working_directory = os.getcwd()

    def get_file_data(self, file_name):
        self.fix_working_directory()
        current_working_directory = os.getcwd()
        file_path = os.path.join(current_working_directory, "resource", file_name)
        file_data = []
        with open(file_path, 'rt') as data_file:
            file_reader = csv.reader(data_file)
            for row in file_reader:
                file_data.append(row)
        return file_data

    def get_last_lines(self, file_name, number_of_lines):
        return self.get_file_data(file_name)[-number_of_lines:]
