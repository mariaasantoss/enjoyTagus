#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 108
# 56918 Francisco Ferreira
# 56915 Maria Santos

from readingFromFiles import *
from dateTime import *
from constants import *

def removeSpace(string):
	"""
    Removes the blank space between words

    Requires:
    string is a str (not null)
    Ensures:
    the same string without white spaces
	"""

	return string.replace(" ", "")

def stringToTuple(str):
	"""
    Transforms a specific string into a tuple

    Requires:
    str != null
    Ensures:
    a tuple with the content of the respective string
	"""

	str = str[1:-1]
	str = removeSpace(str)
	tuplo = str.split(";")
	return tuplo


def orderByDate(line):
	"""
    Goes through a specific line of the schedule, and returns the day of 
    the date of the cruise

    Requires:
    -line is a list contained in the list schedule
    Ensures:
    an int with the day of the date
    """
	return dateToList(line[0])[0]

def orderByHour(line):
	"""
    Goes through a specific line of the schedule, and returns the exact 
    hour of the cruise

    Requires:
    -line is a list contained in the list schedule
    Ensures:
    an int with the exact hour
    """
	return hourToInt(line[1])

def orderByMinute(line):
	"""
    Goes through a specific line of the schedule, and returns the exact 
    minutes of the cruise

    Requires:
    -line is a list contained in the list schedule
    Ensures:
    an int with the exact minute of the cruise
    """
	return minutesToInt(line[1])

def orderBySkipper(line):
	"""
    Goes through a specific line of the schedule, and returns the name 
    of the skipper of that cruise

    Requires:
    -line is a list contained in the list schedule
    Ensures:
    a string with the name of the skipper
    """
	return line[3]

def orderByCost(line):
	"""
    Goes through a specific line of the skipper, and returns the cost
	of the journey for hour

    Requires:
    -line is a list contained in the list skippers
    Ensures:
    an int with the cost of the journey for hour
    """
	return int(line[3])

def orderByHoursWorked(line):
	"""
    Goes through a specific line of the skipper, and returns the hours
	worked or to work until the given time

    Requires:
    -line is a list contained in the list skippers
    Ensures:
    an int with the number of hours worked or to work until the given time
    """
	return int(line[6])

def cleanSchedule(date, hour, schedule):
	"""
    Removes all the cruises that already finished and leaves 
    on the schedule the ones already happening, and the ones
    about to happen

    Requires:
    -date is a str with a specific day
    -hour is a str with a specific hour
    -schedule is a list of lists with the structure as in the output of
    readingFromFiles.readScheduleFile concerning the previous update time;
    Ensures:
    a list of lists with an updated schedule 
    """
	currenthour = hourToInt(hour)
	minute = minutesToInt(hour)
	currentDate = dateToList(date)
	toDelete = []

	for i in range(len(schedule)):
		dateAnalyzed = dateToList(schedule[i][0])
		hourAnalyzed = hourToInt(schedule[i][1])
		minuteAnalyzed = minutesToInt(schedule[i][1])
		durationOfJorney = schedule[i][2]
		inicialHour = hourToInt(schedule[i][1])
		finalHour = int(durationOfJorney) + inicialHour
		if dateAnalyzed[1] == currentDate[1] and dateAnalyzed[0] == currentDate[0]:
			if finalHour <= currenthour:
				if hourAnalyzed < currenthour:
					toDelete.append(i)
				elif hourAnalyzed == currenthour and minuteAnalyzed < minute:
					toDelete.append(i)

		elif dateAnalyzed[1] ==  currentDate[1] and dateAnalyzed[0] < currentDate[0]:
			toDelete.append(i)


	for i in range(len(toDelete)):
		del schedule[0]

	return schedule

def verifyMatch(x,skippers):
	"""
    Verifies if a certain skipper has the match attributes of a certain client, and
	increments the hours of work of the skipper

    Requires:
	-x is a list of lists where each list represents a different request of a certain client
	-skippers is a list of lists where each list represents a different skipper and its attributes
    Ensures:
    list with the skippers and respective clients
	"""
	Aux = []
	result = []
	cont = 0
	lengthList = len(skippers)
	for y in skippers:
		clientLanguage = stringToTuple(x[1])
		skipperLanguage = stringToTuple(y[1])
		for i in clientLanguage:
			if i in skipperLanguage:
				if x[2] == y[2]:
					if x[3] == y[4]:
						skipperWorkHours = int(y[5])
						skipperWorkedHours = int(y[6])
						skipperWorkedHours = skipperWorkedHours + int(x[4])
						if skipperWorkHours >= skipperWorkedHours:
							result.append(True)
							Aux.append(y)
							if len(Aux) > 1:
								Aux = sorted(Aux, key=lambda x: (orderByCost(x), orderByHoursWorked(x), orderBySkipper(x)))
								result.append(Aux[0])
							else:
								for i in Aux:
									result.append(i)
		cont += 1
	if lengthList == cont:
		result.append(False)
		return result
	return result

def process(x,skipper,schedule):
	"""
    Processes all of the skipper/client associations and
	updates the information in the schedule list

    Requires:
    -x is a list of lists where each list represents a different request of a certain client
	-skippers is a list of lists where each list represents a different skipper and its attributes
	-schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
    Ensures:
	an updated list of lists (schedule) with the association skipper/client,
	the respective hours of the cruises and the cost of the cruise
	"""
	totalToPay = int(skipper[3]) * int(x[4])
	travelTime = int(x[4])
	time = skipper[8]
	time = time[:-1]
	lastHour = hourToInt(time)
	minutes = minutesToInt(time)
	endTravelhour = lastHour + travelTime
	diaSeguinte = False
	if minutes == 0:
		minutes = "00"		
	else:
		minutes = "30"						
	if endTravelhour <= 20:
		travelhour = str(lastHour) + ":" + str(minutes)
	else:
		travelhour = "08" + ":" + minutes
		endTravelhour = str(8 + travelTime)
		diaSeguinte = True
	if diaSeguinte == False:
		date = skipper[7]
		if date[0] == "(":
			travelDate = date[1:]
		else:
			travelDate = date
	else:
		date = skipper[7]
		date = dateToList(date)
		date[0] = date[0] + 1
		if date[0] > 30:
			date[0] = 1
			date[1] = date[1] + 1
			if date[1] > 12:
				date[1] = 1
				date[2] = date[2] + 1
		day = str(date[0])
		month = str(date[1])
		if date[0] < 10:
			day = "0" + str(date[0])
		if date[1] < 10:
			month = "0" + str(date[1])
		year = str(date[2])
		travelDate = day + ":" + month + ":" + year

	schedule.append([travelDate, travelhour, str(travelTime), skipper[SKIPPER_NAME_IDX],
		 			str(totalToPay), x[CLIENT_NAME_IDX]])

	return schedule

		

def checkHour(skipper,previousHour):
	"""
    Verifies is the last hour of work of the skipper is smaller
    than the actual time. If it is, updates the hour of the last work
    to the actual hour.


    Requires:
    -skipper is a list with the information of a certain skipper
    -previousHour is a string  with the actual hour
    Ensures:
    a list with the updated hour
    """
	skipperHour = hourToInt(skipper[8])
	hour = hourToInt(previousHour)
	min = previousHour[3:]
	if hour > skipperHour:
		if min == "00":
			min = 30
		skipper[8] = str(hour) + ":" + str(min) +")"
	return skipper

def checkDate(skipper, previousDate, previousHour):
	"""
    Verifies if the last work of the skipper was in the actual day

    Requires:
    -skipper is a list with the information of a certain skipper
    -previousDate is a string with the actual date
    -previousHour is a string  with the actual hour
    Ensures:
    the comparation between the dates is done
    """
	dataAtual = skipper[7]
	dataAtual = dataAtual[1:]
	dataAtual = dateToList(dataAtual)
	dateAux = dateToList(previousDate)
	if dataAtual[0] == dateAux[0]:
		skipper = checkHour(skipper,previousHour)

def updateSchedule(skippers, schedule, requests, previousDate, previousHour):
	"""
        Update cruises' schedule assigning the cruises requested given
        to the skippers given taking into account a previous schedule.
	
	Requires:
	-skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	-schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	-requests is a list of lists with the structure as in the output of 
	readingFromFiles.readRequestsFile concerning the current update time;
	-date is string in format DD:MM:YYYY with the previous update date;
	-hour is string in format HH:MN: with the previous update hour;
	Ensures:
	a list of cruises, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
	"""
	cleanSchedule(previousDate, previousHour, schedule)
	lista = []
	final = []
	for y in requests:
		match = verifyMatch(y,skippers)
		if match[0] == True:
			skipper = match[1]
			checkDate(skipper, previousDate, previousHour)
			process(y,skipper,schedule)
			updateSkippers(skippers,schedule)
		else: 
			date = previousDate
			lista.append([date,NOT_ASSIGNED, y[0]])

	schedule = sorted(schedule, key=lambda x: (orderByDate(x), orderByHour(x), orderByMinute(x), orderBySkipper(x))) 
	
	for i in lista:
		final.append(i)
	for j in schedule:
		final.append(j)
	return final
					

def updateSkippers(skippers, schedule):
	"""
	Update skippers' schedule assigning the cruises requested given
	to the skippers given taking into account a previous schedule.

	Requires:
	-skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	-schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	Ensures:
	a list of cruises, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
	"""
	for i in skippers:
		for j in schedule: 
			if i[SKIPPER_NAME_IDX] in j:
				workedHours = int(i[6]) + int(j[2])
				date = j[0]
				time = j[1]
				hour = hourToInt(time)
				hour = hour + int(j[2])
				min = minutesToInt(time)
				if min == 0:
					min = "00"
				finishTime = str(hour) + ":" + str(min)
				i[6] = str(workedHours)
				i[7] = date
				i[8] = finishTime
	return skippers
				












