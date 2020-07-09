#!/usr/bin/env python3

import csv

data = []

with open('02-2020.csv') as file:
	csv_r = csv.reader(file,  delimiter=';', quotechar='"')
	next(csv_r, None)
	print("Reading: ")
	n = 0
	for r in csv_r:
		#r = r[0].split(";")
		if r[3] == 'NaN':
			r[3] = 0
		if r[4] == 'NaN':
			r[4] = 0
		if r[5] == 'NaN':
			r[5] = 0
		if r[6] == 'NaN':
			r[6] = 0
		n += 1
		if n % 100 == 0:
			print(n, end="\r", flush=True)
		data.append(r)
		
with open('02-2020.cln.csv', mode='w') as file:
	csv_w = csv.writer(file, delimiter=';', quotechar='"')
	print("Writing: ")
	n = 0
	for r in data:
		n += 1
		if n % 100 == 0:
			print(n, end="\r", flush=True)
		csv_w.writerow(r)
