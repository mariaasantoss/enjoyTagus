#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 108
# 56918 Francisco Ferreira
# 56915 Maria Santos


def hourToInt(time):
    """
    Receives the time and returns an integer of the hour

    Requires: 
    time is a str 
    Ensures: 
    the hours as an int
    """
    t = time.split(":")
    return int(t[0])


def minutesToInt(time):
    """
    Receives a certain time and returns an integer of the minutes

    Requires: 
    time is a str
    Ensures:
    the minutes as an int
    """
    t = time.split(":")
    return int(t[1])


def dateToList(date):
    """
    Receives a str and returns the elements separated by : into a list

    Requires: 
    date ir a str
    Ensures:
    a list where each element corresponds to hours and minutes or
    day, month and year
    """
    finalDate = []
    d = date.split(":")
    for i in range(len(d)):
        finalDate.append(int(d[i]))
    return finalDate


def IncrementTime(time):
    """
    Receives a str with a certain time and increments 30 minutes

    Requires: 
    date is a str
    Ensures:
    a str with the given date, 30 minutes ahead
    """
    tHour = hourToInt(time)
    tMin = minutesToInt(time)
    
    if tMin == 30:
        tHour += 1
        tMin = "00"
    else:
        tMin = "30"
    
    finalTime = str(tHour) + ":" + str(tMin)
    return finalTime 


def intToTime(hour, minutes):
    """
    Receives two integers and returns the time as a string

    Requires: 
    hour is an int, minutes is an int
    Ensures:
    the time in a string in format HH:MN
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m










