#Imports
import sys
import datetime

#Store arguments in local variables
filePath = sys.argv[1]
interval = sys.argv[2]

#Set variables
current = None
delta = datetime.timedelta(minutes=int(interval))
count = 0
result = []

#Get all timestamps
f = open(filePath, "r")
lines = f.readlines()
f.close()

current = datetime.datetime.strptime(lines[0].strip(), '%Y-%m-%d %H:%M:%S')

for line in lines:
    line = line.strip()
    datetime_obj = datetime.datetime.strptime(line, '%Y-%m-%d %H:%M:%S')

    if (datetime_obj - current) <= delta:
        count += 1
    else:
        result.append((current, count))
        current = datetime_obj
        count = 1
result.append((current, count))

for res in result:
    print res
