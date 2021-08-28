#!/usr/bin/python

from urllib.request import urlopen

def downloadDataToFile(url, filename):
    """Download url and save to file"""
    answer = input("Letölti a fájlt? Y/N: ").upper()
    if answer == "Y":
        print(f"Download {filename} ...")
        with open(filename,'wb') as f:
            f.write(urlopen(url).read())


def loadDataFromFile(filename):
    data = []
    with open(filename,'rt') as f:
        for line in f:
            data.append(line.strip().split(';'))
    data.reverse()
    return data


def createStatistic(data,column_numbers,max_num):
    """Return list"""
    num_count = column_numbers[1]-column_numbers[0] # Hány kiirandó szám van?

    statistic = [] # A visszaadandó táblázat
    #Feltöltünk num_count számú tömböt
    for i in range(num_count+1):
        statistic.append([0]*(max_num+1))

    for line in data:
        num_list = line[column_numbers[0]: column_numbers[1]]
        num_list = list(map(int,num_list))
        for index in range(num_count):
            act_num = num_list[index]
            statistic[index][act_num]= statistic[index][act_num]+1

    return statistic


def printStatistic(statistic, max_num):
    for r in range(max_num+1):
        print(f"{r:3}> ", end='')
        for c in range(len(statistic)):
            print(f"{statistic[c][r]:>4}|", end=' ')
        print()

def szazalek(alap, ertek):
    print(f"{alap}/{ertek} - {ertek/alap*100:3}%")

 
