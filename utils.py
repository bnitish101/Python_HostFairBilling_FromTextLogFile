import sys
from datetime import datetime
from os.path import isfile


def getFile():
    if len(sys.argv) == 2:
        # Correct Command Line Arguments

        path_to_file = sys.argv[1]
        if isfile(path_to_file):
            # File exists

            path_to_file_list = path_to_file.split('.')
            if len(path_to_file_list) > 1 and path_to_file_list[-1] == 'txt':
                # File type is txt

                return sys.argv[1]
            else:
                # File type is not txt

                print("\n<"+path_to_file+"> Incorrect file type, accepts txt file type only.")
                quit()
        else:
            # File doesn't exist

            print("\n<"+path_to_file+"> File doesn't exist!")
            quit()
    else:
        # Incorrect Command Line Arguments

        print("\nIncorrect argument for Log File Path!")
        quit()


def getTimeDurationInSecond(startTime="", endTime=""):
    return (datetime.strptime(endTime, '%H:%M:%S') - datetime.strptime(startTime, '%H:%M:%S')).seconds

