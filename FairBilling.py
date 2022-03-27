from readTextFile import *
from FairBillingOperations import *
from utils import *

file = getFile()
result_logData = filterFileData(file)

if result_logData['result']['status'] == 'success' and len(result_logData['result']['logData']) > 0:
    logData = result_logData['result']['logData']

    result_user_session_details = FairBillingOperation(logData)

    print()
    for user_session_detail in result_user_session_details:
        print(user_session_detail[0], user_session_detail[1], user_session_detail[2])

    print()
    input('Press Enter to exit!')

else:
    print('\n', result_logData['result']['status'])
    print(result_logData['result']['message'])
    print('Data Not found!')
