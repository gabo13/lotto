#!/usr/bin/python

import kozos

# A következő mezők kitöltése kötelező:
link = "https://bet.szerencsejatek.hu/cmsfiles/hatos.csv"
column_numbers = 13,19
max_num = 45
#-------------------------------------
print("***** HATOS LOTTO *****")
kozos.downloadDataToFile(link,"hatos.csv")
data = kozos.loadDataFromFile("hatos.csv")
print("Adatszerkezet:")
print(data[0])
print("A számok:")
print(data[0][column_numbers[0]:column_numbers[1]])
print("Összes sorsolás: ",len(data))
statistic = kozos.createStatistic(data,column_numbers,max_num)
print("Statisztika:")
kozos.printStatistic(statistic, max_num)
