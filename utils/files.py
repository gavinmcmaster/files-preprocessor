import re
import os


def get_valid_files(dir):
    files = []
    for filename in os.listdir(dir):
        if filename.endswith(".csv"):
            file = File(filename)
            if file.has_valid_filename():
                files.append(file)
    return files


def get_client_files(idnumber, files):
    client_files = []
    for file in files:
        client_idnumber = file.name.split('_')[0].lower()
        print(f'client file: {client_idnumber}, idnumber: {idnumber}')
        if client_idnumber == idnumber:
            client_files.append(file)

    return client_files


class File:
    CSV_REGEX = "[a-zA-Z]+\d+_(user|pos|org)\.csv"
    VALID_TYPES = ['user', 'pos', 'org']

    def __init__(self, name):
        self.name = name

    def has_valid_filename(self):
        if re.match(self.CSV_REGEX, self.name):
            return True

        return False
