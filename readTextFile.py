from datetime import datetime


def filterFileData(file):
    logData = []
    try:
        f = open(str(file), 'r')
        for line in f:

            current_line = {}  # {'time': '14:02:03', 'user': 'ALICE99', 'session': 'Start'}
            words = line.split()
            # validations on: time, user, session
            if (len(words) == 3) and (words[1].isalnum() and len(words[1]) == 7) and (
                    words[2] == 'Start' or words[2] == 'End'):
                try:
                    datetime.strptime(words[0], '%H:%M:%S')
                    if words[1] != '':
                        current_line['time'] = words[0]
                        current_line['user'] = words[1]
                        current_line['session'] = words[2]
                        logData.append(current_line)
                except:
                    None

        f.close()
        status = 'success'
        message = "<" + file + "> Log File read."
    except:
        status = 'fail'
        message = "<" + file + "> Log File can't read."

    return {'result': {'status': status, 'message': message, 'logData': logData}}
