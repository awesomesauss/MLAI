from FileHandler import FileHandler
import csv


class CsvFile(FileHandler):
    def read(self):
        # TODO:
        # Read all rows from the CSV file and return them as a list
        x = []
        with open(self.filepath, mode = 'r', newline ='') as file:
            reader = csv.reader(file)
            for row in reader:
               x.append(row)
        return x
