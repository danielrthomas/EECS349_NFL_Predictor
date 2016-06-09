#####################################################################################################
##		This file aims to take in the dataset of running averages and analyze it further by adding
##	attributes to represent trends or patterns that may help predict future games.
##  Daniel Thomas, Thornton Uhl, Scott Renshaw



import csv, collections
import random

## This function reads from a desired file and returns the 2D List
def read(pathname,size):
    data = []
    datafile = open(pathname, 'rU')
    datareader = csv.reader(datafile, dialect = 'excel')
    for i in range(513):
    	data.append([])
    	point = datareader.next()
    	for j in range(size):
    		data[i].append(point[j])

    return data

##  This function writes a given 2D array to a dataset.csv
def write_data(data):
	fl = open('dataset.csv', 'w')
	writer = csv.writer(fl)
	for values in data:
		writer.writerow(values)
	fl.close()

## This function stores the difference between the average number of points a team scored
# up until this week and the average number of points a team scored up to the week before
# d_Tm(x) = Tm(x) - Tm(x-1)
def add_d_Tm():
	season = 16
	data_w_label = read('2015_NFL_W_M.csv',19)
	data_w_label[0].insert(len(data_w_label[0])-1,'d_Tm')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		if x % season == 0:
			value = 0
		else:
			value = float(data[x][2])*(x+1) - float(data[x-1][2])*x
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function does the same as the attribute above, but for the points scored against any given team
# d_OppS(x) = OppS(x) - OppS(x-1)
def add_d_OppS():
	season = 16
	data_w_label = read('dataset.csv',20)
	data_w_label[0].insert(len(data_w_label[0])-1,'d_OppS')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		if x % season == 0:
			value = 0
		else:
			value = float(data[x][3]) - float(data[x-1][3])
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function aims to find the scoring momentum a team has achieved on any given week by summing the
# last 3 average score differentials
# scoring_momentum3(x) = Tm(x) + Tm(x-1) + Tm(x-2) - OppS(x) - OppS(x-1) - OppS(x-2)
def add_scoring_momentum3():
	season = 16
	data_w_label = read('dataset.csv',21)
	data_w_label[0].insert(len(data_w_label[0])-1,'scoring_momentum3')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		value = float(data[x][2]) - float(data[x][3])
		if x % season == 0:
			value *= 3
		elif x % season == 1:
			value += float(data[x - 1][19])/3
			value *= 1.5
		else:
			value += float(data[x - 1][19])/3 + float(data[x - 2][19])/3
		data[x].insert(len(data[x])-1,value)
	data_w_label[1:] = data
	return data_w_label

## This function aims to find the turnover momentum a team has achieved on any given week by summing the
# last 3 average turnover differentials
# turnover_momentum3(x) = DTO(x) + DTO(x-1) + DTO(x-2) - OTO(x) - OTO(x-1) - OTO(x-2)
def add_turnover_momentum3():
	season = 16
	data_w_label = read('dataset.csv',22)
	data_w_label[0].insert(len(data_w_label[0])-1,'turnover_momentum3')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		value = float(data[x][13]) - float(data[x][8])
		if x % season == 0:
			value *= 30
		elif x % season == 1:
			value += float(data[x - 1][20])/30
			value *= 15
		else:
			value += float(data[x - 1][20])/30 + float(data[x - 2][20])/30
		data[x].insert(len(data[x])-1,10*value)
	data_w_label[1:] = data
	return data_w_label

## This function aims to find the scoring momentum a team has achieved on any given week by summing the
# last 4 average score differentials
# scoring_momentum3(x) = Tm(x) + Tm(x-1) + Tm(x-2) + Tm(x-3) - OppS(x) - OppS(x-1) - OppS(x-2) - OppS(x-3)
def add_scoring_momentum4():
	season = 16
	data_w_label = read('dataset.csv',23)
	data_w_label[0].insert(len(data_w_label[0])-1,'scoring_momentum4')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		value = float(data[x][2]) - float(data[x][3])
		if x % season == 0:
			value *= 4
		elif x % season == 1:
			value += float(data[x - 1][21])/4
			value *= 2
		elif x % season == 2:
			value += float(data[x - 1][21])/4 + float(data[x - 2][21])/4
			value *= 4/3
		else:
			value += float(data[x - 1][21])/4 + float(data[x - 2][21])/4 + float(data[x - 3][21])/4
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function aims to find the turnover momentum a team has achieved on any given week by summing the
# last 3 average turnover differentials
# turnover_momentum3(x) = DTO(x) + DTO(x-1) + DTO(x-2) + DTO(x-3) - OTO(x) - OTO(x-1) - OTO(x-2) - OTO(x-3)
def add_turnover_momentum4():
	season = 16
	data_w_label = read('dataset.csv',24)
	data_w_label[0].insert(len(data_w_label[0])-1,'turnover_momentum4')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		value = float(data[x][13]) - float(data[x][8])
		if x % season == 0:
			value *= 40
		elif x % season == 1:
			value += float(data[x - 1][22])/40
			value *= 20
		elif x % season == 2:
			value += float(data[x - 1][22])/40 + float(data[x - 2][22])/40
			value *= 40/30
		else:
			value += float(data[x - 1][22])/40 + float(data[x - 2][22])/40 + float(data[x - 3][22])/40
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function stores the difference between the average number of 1st downs a team achieved
# up until this week and the average number of 1st downs a team achieved up to the week before
# d_O1stD(x) = O1stD(x) - O1stD(x-1)
def add_d_O1stD():
	season = 16
	data_w_label = read('dataset.csv',25)
	data_w_label[0].insert(len(data_w_label[0])-1,'d_O1stD')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		if x % season == 0:
			value = 0
		else:
			value = float(data[x][4]) - float(data[x-1][4])
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function stores the difference between the average number of total offensive yards a team achieved
# up until this week and the average number of offensive total yards a team achieved up to the week before
# d_OTotYd(x) = OTotYd(x) - OTotYd(x-1)
def add_d_OTotYd():
	season = 16
	data_w_label = read('dataset.csv',26)
	data_w_label[0].insert(len(data_w_label[0])-1,'d_OTotYd')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		if x % season == 0:
			value = 0
		else:
			value = float(data[x][5]) - float(data[x-1][5])
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function stores the difference between average total offensive yards up until this game and average
# yards allowed up until this game
# yard_differential(x) = OTotYd(x) - DTotYd(x)
def add_yard_differential():
	season = 16
	data_w_label = read('dataset.csv',27)
	data_w_label[0].insert(len(data_w_label[0])-1,'yard_differential')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		value = float(data[x][5]) - float(data[x][10])
		data[x].insert(len(data[x])-1,value)

	data_w_label[1:] = data
	return data_w_label

## This function iteratively stores the win/loss differntial a team has until this game by starting an integer at 0.
# Each datapoint updates with the previous game's result as wins = +1 and losses = -1
# wl(0) = 0
# wl(x) = wl(x-1) +/-1  (depending on W or L result(x-1))
def add_wl():
	season = 16
	data_w_label = read('dataset.csv',27)
	data_w_label[0].insert(len(data_w_label[0])-1,'w_l')
	data = data_w_label[1:]
	for x in range(len(data[1:]) + 1):
		if x % season == 0:
			value = 0
		else:
			value = float(data[x-1][26]) #/x
			if data[x-1][27] == 'L':
				value -= 1
			elif data[x-1][27] == 'W':
				value += 1
		data[x].insert(len(data[x])-1,value)
	data_w_label[1:] = data
	return data_w_label


## This function takes the dataset we generated of running averages and adds the analytical attributes one at a time
def make_data():
	write_data(add_d_Tm())
	write_data(add_d_OppS())
	write_data(add_scoring_momentum3())
	write_data(add_turnover_momentum3())
	write_data(add_scoring_momentum4())
	write_data(add_turnover_momentum4())
	write_data(add_d_O1stD())
	write_data(add_d_OTotYd())
	# write_data(add_yard_differential())
	write_data(add_wl())
