#!/usr/bin/python
import kozos

# A következő mezők kitöltése kötelező:
link = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"
column_numbers = 11,16
max_num = 90
#-------------------------------------
print("***** ÖTÖS LOTTO *****")
kozos.downloadDataToFile(link,"otos.csv")
data = kozos.loadDataFromFile("otos.csv")
print("Adatszerkezet:")
print(data[0])
print("A számok:")
print(data[0][column_numbers[0]:column_numbers[1]])
print("Összes sorsolás: ",len(data))
statistic = kozos.createStatistic(data,column_numbers,max_num)
print("Statisztika:")
kozos.printStatistic(statistic, max_num)
