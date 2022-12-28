#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 108
# 56918 Francisco Ferreira
# 56915 Maria Santos

import sys
from readingFromFiles import *
from scheduling import *
from writingToFiles import *

def assign(skippersFileName, scheduleFileName, requestsFileName):
    """
    Runs the enjoyTagus application.

    Requires:
    skippersFileName is a str with the name of a .txt file containing a list
    of skippers, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of cruises assigned to skippers as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested;
    these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the updated list of cruises assigned
    to skippers and the updated list of skippers, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    skippersXXhYY.txt, where XXhYY represents the time and date 30 minutes
    after the time and date indicated in the files skippersFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    try: 
        newSchedule =(updateSchedule(readSkippersFile(skippersFileName),
        readScheduleFile(scheduleFileName), 
        readRequestsFile(requestsFileName), 
        getHeaderInfo(scheduleFileName)[1], 
        getHeaderInfo(scheduleFileName)[2]))

        copy = newSchedule.copy()
        originalSchedule = readScheduleFile(scheduleFileName)
        toRemove = []
        for i in copy:
            if i in originalSchedule:
                toRemove.append(i)
        if toRemove != []:
            for i in toRemove:
                copy.remove(i)

        newSkipperList = updateSkippers(readSkippersFile(skippersFileName),copy)


        timeFileName1 = IncrementTime(getHeaderInfo(scheduleFileName)[2]) 
        header = "Company: \n" + getHeaderInfo(scheduleFileName)[0] + "\n" + \
        "Day: \n" + getHeaderInfo(scheduleFileName)[1] + "\n" + \
        "Time: \n" + timeFileName1 + "\n" + getHeaderInfo(scheduleFileName)[3][:-1]

        fileName1 = "s" + getHeaderInfo(scheduleFileName)[3][1:-2] +timeFileName1[:2] + 'h' + timeFileName1[3:] + ".txt"
        writeScheduleFile(newSchedule, header, fileName1)

        timeFileName2 = IncrementTime(getHeaderInfo(skippersFileName)[2]) 
        fileName2 = "s" + getHeaderInfo(skippersFileName)[3][1:-2] +timeFileName2[:2] + 'h' + timeFileName2[3:] + ".txt"
        writeSkippersFile(newSkipperList, header, fileName2)

    except AssertionError:
        print("Scope or time inconsistency between name and header in file <name of file>")


assign(sys.argv[1],sys.argv[2],sys.argv[3])    

