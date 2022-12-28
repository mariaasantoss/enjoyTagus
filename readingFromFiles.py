#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 108
# 56918 Francisco Ferreira
# 56915 Maria Santos

from constants import *

def getHeaderInfo(fileName):
    """
    Reads a specific file, gets the header information of the respective file
    and puts it into a list

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers, requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list where each element of the list corresponds to a specific information of the 
    header following the order provided in the lines of the file.
    """
    info = []
    inFile =  open(fileName, 'r')
    content =inFile.readlines()
    company = content[1]
    company = company[:-1]
    day = content[3]
    day = day[:-1]
    time = content[5]
    time = time[:-1]   
    type = content[6] 

    info.append(company)
    info.append(day)
    info.append(time)
    info.append(type)

    return info


def removeHeader(fileName):
    """
    Reads a specific file and removes its header

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers or requests, or a schedule organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    file without the header lines
    """
    inFile =  open(fileName, 'r')
    data = inFile.read().splitlines(True)
    if data[0] == "Company:\n":
        outFile =  open(fileName, 'w')
        outFile.writelines(data[7:])

        
def getInfo(fileName):
    """
    Reads a specific file and removes its header

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers or requests, or a schedule organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list os lists where each list is a line of the input file and each element
    of the list corresponds to a specific information
    """
    header = []
    info = []
    inFile =  open(fileName, 'r')
    content = inFile.read().splitlines(True)
    header.append(content[0:NUM_HEADER_LINES])
    info.append(content[NUM_HEADER_LINES:])

    removeHeader(fileName)

    inFile2 =  open(fileName, 'r')
    content2 = inFile2.read().splitlines(True)
    infoList = [] 
    for line in content2:
        data = line.rstrip().split(", ")
        infoList.append(data)

    final = open(fileName, 'w')
    for i in header:
        final.writelines(i)
    for j in info:
        final.writelines(j)

    return infoList


def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    skippersList = getInfo(fileName)   
    return skippersList


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that request),
    following the order provided in the lines of the file.
    """
    requestsList = getInfo(fileName)
    return requestsList


def readScheduleFile(fileName):
    """"
    Reads a file with a list of scheduled cruises with a given file name into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of a schedule organized as in the examples provided in
    the general specification (omitted here for the sake of readability).

    Ensures:
    list of lists where each list corresponds to a shcedule listed in
    the file fileName (with all the info pieces belonging to that request),
    following the order provided in the lines of the file.
    """
    scheduleList = getInfo(fileName)
    return scheduleList

   