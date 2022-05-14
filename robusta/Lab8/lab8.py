import random as rd
import csv

class myFunc:
    def random_number_generator(self, input):
        self.l_array=[]
        for i in range(0, input):
            e = rd.randint(0, i)
            self.l_array.append(e)

        return self.l_array

    def random_number(input):
        l_array=[]
        for i in range(0, input):
            e = rd.randint(0, i)
            l_array.append(e)

        return l_array

# if __name__ == '__main__':
#     a= random_number_generator(10)
#     print(a)

class myFile:
    def readFileCSV(self, filePath):
        with open(filePath, 'r') as f:
            mock_data_reader = csv.reader(f)
            self.line_count = 1
            for row in mock_data_reader:
                if self.line_count < 10:
                    print(row)
                self.line_count += 1

    def writeRowCSV(self, filePath):
        with open(filePath, 'w') as f:
            ew = csv.writer(f)
            ew.writerow(['name', 'age'])
            ew.writerow(['Steven', 25])

    def dictWriterCSV(self, filePath):
        with open(filePath, 'w') as f:
            fields = ['name', 'age']
            ew = csv.DictWriter(f, fieldnames=fields)
            ew.writeheader()
            ew.writerow({'name': 'Steven', 'age': 1000})

        

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age