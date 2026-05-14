from FileHandler import FileHandler
import json


class JsonFile(FileHandler):
    def read(self):
        # TODO:
        # Open the JSON file and return the Python object
        with open(self.filepath, mode = 'r') as file:
            data = json.load(file)
        return data 
