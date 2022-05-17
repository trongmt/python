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

import numpy as np
import array as arr
class myNumpy:
    def sample1(self):
        self.ls1 = [1,2]
        larr = np.array(self.ls1)
        print(larr)

        a = arr.array('d', [1,2,3,4,5.6])
        print(a)

    def sample2(self, input):
        print("Since:", np.sin(input))
        print("Natural:", np.log(input))
        print("Base-10 logarithm:", np.log10(input))
        print("Base-2 logarithm:", np.log2(input))

    def sample3(self):
        print("Numbers spaced apart by 2: np.arange(0, 11, 2) -> ", np.arange(0, 11, 2))
        print("Numbers spaced apart by a floating point number: np.arange(0, 11, 2.5) -> ", np.arange(0, 11, 2.5))
        print("Every 5th number from 30 in reverse order: np.arange(30, -1, -5) -> ", np.arange(30, -1, -5))
        print("11 linearly spaced numbers between 1 and 5: np.linspace(1, 5, 11) -> ", np.linspace(1, 5, 11))

    def sample4(self):
        array_1 = np.arange(0, 11)
        print("Array:",array_1)
        print("Element at 7th index is:", array_1[7])
        print("Elements from 3rd to 5th index are:", array_1[3:6])
        print("Elements up to 4th index are:", array_1[:4])
        print("Elements from last backwards are:", array_1[-1::-1])
        print("3 Elements from last backwards are:", array_1[-1:-6:-2])

        array_2 = np.arange(0,21,2)
        print("New array:",array_2)
        print("Elements at 2nd, 4th, and 9th index are:", array_2[[2,4,9]])
        matrix_1 = np.random.randint(10,100,15).reshape(3,5)
        print("Matrix of random 2-digit numbers\n ",matrix_1)

        print("\nDouble bracket indexing\n")
        print("Element in row index 1 and column index 2:", matrix_1[1][2])



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age