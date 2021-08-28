#!/usr/bin/python

import kozos
from datetime import datetime
# A következő mezők kitöltése kötelező:
link = "https://bet.szerencsejatek.hu/cmsfiles/skandi.csv"
column_numbers = 11,25
max_num = 35
#-------------------------------------
print("***** SKANDINÁV LOTTO *****")
kozos.downloadDataToFile(link,"skandi.csv")
data = kozos.loadDataFromFile("skandi.csv")
print("Adatszerkezet:")
print(data[0])
print("A számok:")
print(data[0][column_numbers[0]:column_numbers[1]])
print("Kiértékelve: ",datetime.now())
print("Összes sorsolás: ",len(data))
statistic = kozos.createStatistic(data,column_numbers,max_num)
for i in range(7):
    statistic[i][0] = "K"+str(i+1)
    statistic[i+7][0] = "G"+str(i+1)
statistic[14][0] = "SUM"
for r in range(1,36):
    sum = 0
    for c in range(14):
        sum = sum+ statistic[c][r]
    statistic[14][r] = sum
print("Statisztika:")
kozos.printStatistic(statistic, max_num)

