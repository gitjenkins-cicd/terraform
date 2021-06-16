# LCF

# import calendar
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
#
# print(calendar.month(yy,mm))

# import time
# import sys
#
# while True:
#     from datetime import datetime
#     now = datetime.now()
#     print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)),
#     sys.stdout.flush()
#     print("\r"),
#     time.sleep(1)
#
# i=1
# j=0
import itertools
for i in itertools.count():
    # print (i)
    with open('file1.txt','a') as f:
        f.write(str(i))

    # break