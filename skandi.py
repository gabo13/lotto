#!/usr/bin/python

import kozos
from datetime import datetime
# A következő mezők kitöltése kötelező:
filename = "skandi.csv"
link = "https://bet.szerencsejatek.hu/cmsfiles/"+ filename

column_numbers = 11, 25
kezi = 11, 18
gepi = 18, 25
max_num = 35
kozos.downloadDataToFile(link,filename)
data = kozos.loadDataFromFile(filename)
huzasok = len(data)
#-------------------------------------
def get_kezi(l):
    return kozos.getSubList(l,kezi[0],kezi[1])

def get_gepi(l):
    return kozos.getSubList(l,gepi[0],gepi[1])
#-------------------------------------
print("***** SKANDINÁV LOTTO *****")
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

szelveny = kozos.load_szelveny("skandi.txt")
print("Szelvény:")
beja=[2,7,15,35,9,26,8,31]
beja=[19,28,6,11,25,26,16]
szelveny.append(list(map(str,beja)))
print(szelveny)
for huzas in szelveny:
    print(f"Mezo{szelveny.index(huzas)+1}.)", *huzas)
    for line in data:
        kezi_szamok = get_kezi(line)
        talalat = kozos.talalat(kezi_szamok, huzas)
        if len(talalat) > 3:
            print("\t", *talalat, "\tTalálat: ", len(talalat))
#print("Kezi: ", data[0][kezi[0]:kezi[1]])
#print("Gépi: ", data[0][gepi[0]:gepi[1]])


