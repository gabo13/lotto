#!/usr/bin/python

import kozos

# A következő mezők kitöltése kötelező:
link = "https://bet.szerencsejatek.hu/cmsfiles/skandi.csv"
column_numbers = 11,25
max_num = 35
#-------------------------------------
print("***** SKANDINÁV LOTTO *****")
#kozos.downloadDataToFile(link,"skandi.csv")
data = kozos.loadDataFromFile("skandi.csv")
print("Adatszerkezet:")
print(data[0])
print("A számok:")
print(data[0][column_numbers[0]:column_numbers[1]])
print("Összes sorsolás: ",len(data))
statistic = kozos.createStatistic(data,column_numbers,max_num)
print("Statisztika:")
kozos.printStatistic(statistic, max_num)
