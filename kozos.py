#!/usr/bin/python

from urllib.request import urlopen

def downloadDataToFile(url, filename):
    """
    Download url and save to file
    url:
    filename: filename to save data
    """
    
    answer = input("Letölti a fájlt? Y/N: ").upper()
    if answer == "Y":
        print(f"Download {filename} ...")
        with open(filename,'wb') as f:
            f.write(urlopen(url).read())


def loadDataFromFile(filename):
    """
    Load  data from file
    filename: open csv file and create list
    """
    data = []
    with open(filename,'rt') as f:
        for line in f:
            data.append(line.strip().split(';'))
    data.reverse()
    return data


def createStatistic(data,column_numbers,max_num):
    """
    Generate statistic from data
    data: 2 dimensional list
    column_numbers: 2 integer in tuple, first column and last column+1
    max_num: largest number in numbers
    """
    num_count = column_numbers[1]-column_numbers[0] # Hány kiirandó szám van?

    statistic = [] # A visszaadandó táblázat
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
    print("Statisztika:")
    for r in range(max_num+1):
        print(f"{r:3}> ", end='')
        for c in range(len(statistic)):
            print(f"{statistic[c][r]:>4}|", end=' ')
        print()

def szazalek(alap, ertek):
    print(f"{alap}/{ertek} - {ertek/alap*100:3}%")

def talalat(iterable1, iterable2):
    """
    Return 2 iterables intersection
    """
    s1=set(iterable1)
    s2=set(iterable2)
    return s1.intersection(s2)

def getSubList(l, s, e):
    """
    Return l iterable sublist
    """
    return l[s:e]

def load_szelveny(filename):
    """
    Load 2 dimensional list from lotto ticket
    """
    l = []
    print("Szelvény: ")
    with open(filename,"rt") as f:
        for line in f:
            szamok = line.strip().split(" ")
            l.append(szamok)
            print(*szamok)
    return l

def talalat2(huzas, data, numbers_func, min_talalat = 4):
    """ huzas: numbers from lotto ticket
        data: csv file data
        numeric_func: numbers from csv file line
        min_talalat: smalest hits
    """
    stat = {4:0, 5:0, 6:0, 7:0}
    for line in data:
        szamok = numbers_func(line)
        talalatok = talalat(szamok, huzas)
        if len(talalatok) >= min_talalat:
            #print(*talalatok, "\tTalálat: ", len(talalatok))
            try:
                stat[len(talalatok)] = stat[len(talalatok)] +1
            except KeyError as e:
                stat[int(str(e))]=1
    return stat
