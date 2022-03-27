Fair billing (Calculate the charge per second of usage)

Development Environment interpreter on
Python 3.10.1

To demonstrate, sessionsLog.txt file can be used.
<Execution instructions from cmd>

<with Command Line Arguments>
python FairBilling.py logFilePath

<eg.
C:\PythonPractice\Python\HostFairBilling>python FairBilling.py C:/PythonPractice/Python/HostFairBilling/sessionsLog.txt
>
<eg.
after file data filtered logData>>
[{'time': '14:02:03', 'user': 'ALICE99', 'session': 'Start'}, {'time': '14:02:05', 'user': 'CHARLIE', 'session': 'End'}, {'time': '14:02:34', 'user': 'ALICE99', 'session': 'End'}, {'time': '14:02:58', 'user': 'ALICE99', 'session': 'Start'}, {'time': '14:03:02', 'user': 'CHARLIE', 'session': 'Start'}, {'time': '14:03:33', 'user': 'ALICE99', 'session': 'Start'}, {'time': '14:03:35', 'user': 'ALICE99', 'session': 'End'}, {'time': '14:03:37', 'user': 'CHARLIE', 'session': 'End'}, {'time': '14:04:05', 'user': 'ALICE99', 'session': 'End'}, {'time': '14:04:23', 'user': 'ALICE99', 'session': 'End'}, {'time': '14:04:41', 'user': 'CHARLIE', 'session': 'Start'}]
>

<Putting this all together, the results for the original data would be as follows (name, sessions and total time)>
<Output>
userName userSession userTotalUsageInSeconds

<eg.
ALICE99 4 240
CHARLIE 3 37
>