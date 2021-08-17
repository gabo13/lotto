#!/usr/bin/python

from urllib.request import urlopen


def downloadDataToFile(url, filename):
	"""Download url and save to file"""

	with open(filename,'wb') as f:
		f.write(urlopen(url).read())


def loadDataFromFile(filename):
	data = []
	with open(filename,'rt') as f:
		for line in f:
			data.append(line.strip().split(';'))
	return data


