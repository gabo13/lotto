#!/usr/bin/python

import kozos
from datetime import datetime
# A következő mezők kitöltése kötelező:
filename = "skandi.csv"
link = "https://bet.szerencsejatek.hu/cmsfiles/"+ filename

column_numbers = 11, 25
k1, k7 = 11, 18 # 11-17
g1, g7 = 18, 25 # 18-24
max_num = 35
kozos.downloadDataToFile(link,filename)
data = kozos.loadDataFromFile(filename)
huzasok = len(data)
#-------------------------------------
def get_kezi(l):
    return kozos.getSubList(l,k1,k7)

def get_gepi(l):
    return kozos.getSubList(l,g1,g7)
#-------------------------------------
print("***** SKANDINÁV LOTTO *****")
print("Adatszerkezet:")
print(data[0])
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

szelveny = kozos.load_szelveny("skandi.txt")
print("Kezi: ")
#k = kozos.talalat2(szelveny[0],data,get_kezi)
#print(k)
print("Gépi: ")
g = kozos.talalat2(szelveny[0],data,get_gepi)
print(g)

