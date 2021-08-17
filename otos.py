#!/usr/bin/python

import kozos

link = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"
numbers = 11,15

kozos.downloadDataToFile(link,"otos.csv")
data = kozos.loadDataFromFile("otos.csv")
print(data[0])
print(data[0][numbers[0]:])

