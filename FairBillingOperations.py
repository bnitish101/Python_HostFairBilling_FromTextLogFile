from utils import *


def FairBillingOperation(logData):
    user_session_detail = {}
    initStartTime = logData[0]['time']
    initEndTime = logData[-1]['time']

    for data in logData:

        user_name = data['user']
        if user_name not in user_session_detail:
            # new user

            # initialize dict for new user wrt user_name
            user_session_detail[user_name] = {'session_count': 0, 'duration': 0, 'session_start': []}

            if data['session'] == 'End':
                # Session End
                user_session_detail[user_name]['session_count'] = 1

                # ------------- cb+ s (time calculation) ------------- #
                duration_in_seconds = getTimeDurationInSecond(initStartTime, data['time'])
                # ------------- cb+ e (time calculation) ------------- #
                user_session_detail[user_name]['duration'] += duration_in_seconds

            else:
                # Session Start
                user_session_detail[user_name]['session_start'].append(data['time'])

        else:
            # existing user
            if data['session'] == 'End':
                # Session End
                user_session_detail[user_name]['session_count'] += 1
                if len(user_session_detail[user_name]['session_start']) > 0:
                    # User with Start Session
                    # ------------- cb+ s (time calculation) ------------- #
                    startTime = user_session_detail[user_name]['session_start'][0]
                    duration_in_seconds = getTimeDurationInSecond(startTime, data['time'])
                    # ------------- cb+ e (time calculation) ------------- #

                    user_session_detail[user_name]['duration'] += duration_in_seconds
                    del user_session_detail[user_name]['session_start'][0]  # delete the used session start_time (first)
                else:
                    # User without Start Session
                    # ------------- cb+ s (time calculation) ------------- #
                    duration_in_seconds = getTimeDurationInSecond(initStartTime, data['time'])
                    # ------------- cb+ e (time calculation) ------------- #

                    user_session_detail[user_name]['duration'] += duration_in_seconds

            else:
                # Session Start
                user_session_detail[user_name]['session_start'].append(data['time'])

    result_user_session_details = []
    for user in user_session_detail:

        if len(user_session_detail[user]['session_start']) > 0:
            # add duration and session for all remaining start sessions
            for session_start in user_session_detail[user]['session_start']:
                user_session_detail[user]['session_count'] += 1

                # ------------- cb+ s (time calculation) ------------- #
                duration_in_seconds = getTimeDurationInSecond(session_start, initEndTime)
                # ------------- cb+ e (time calculation) ------------- #

                user_session_detail[user]['duration'] += duration_in_seconds

        result_user_session_details.append(
            (user, user_session_detail[user]['session_count'], user_session_detail[user]['duration'])
        )

    return result_user_session_details
