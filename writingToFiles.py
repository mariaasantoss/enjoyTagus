#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 108
# 56918 Francisco Ferreira
# 56915 Maria Santos


def writeScheduleFile(schedule, header, fileName):
    """
    Writes a collection of scheduled cruises into a file.

    Requires:
    schedule is a list with the structure as in the output of
    scheduling.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the cruises in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the cruises as ordered head to tail in schedule.
    """
    outFile = open(fileName, "w")
    outFile.write(header + "\n")
    for i in schedule:
        outFile.write(str(i)[1:-1] + " \n")



def writeSkippersFile(skippers, header, fileName):
    """
    Writes a collection of scheduled skippers into a file.

    Requires:
    skippers is a list with the structure as in the output of
    scheduling.updateSkippers representing the skippers assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the skippers in schedule and
    respective cruises, one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the cruises as ordered head to tail in schedule.
    """
    outFile = open(fileName, "w")
    outFile.write(header + "\n")
    for i in skippers:
        outFile.write(str(i)[1:-1] + " \n")
