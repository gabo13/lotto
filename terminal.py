#!/usr/bin/python

import kozos
from os import system

def printmenu():
    sytem("clear")
    print(" 1.) Ötös lotto")
    print(" 2.) Hatos lotto")
    print(" 3.) Skandináv lotto")
    return input("Kérek egy számot: ")

str = printmenu()

if str == "1":
    link = "https://bet.szerencsejatek.hu/csvfiles/otos.csv"
    column_numbers = 11,16
    max_num = 90
elif str == "2":
    link = "https://bet.szerencsejatek.hu/csvfiles/hatos.csv"
    column_numbers = 11,16
    max_num = 45
elif str == "3":
    link = "https://bet.szerencsejatek.hu/csvfiles/skandi.csv"
    column_numbers = 11,16
    max_num = 35
else:
    print
