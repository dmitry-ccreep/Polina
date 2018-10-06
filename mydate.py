import sys
import datetime

while True:
    sys.stdout.write('\r' + str(datetime.datetime.now()))
    sys.stdout.flush()
