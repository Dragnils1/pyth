# time([hour] [, min] [, sec] [, microsec])
from datetime import time
 
current_time = time()
print(current_time)     # 00:00:00
 
current_time = time(16, 25)
print(current_time)     # 16:25:00
 
current_time = time(16, 25, 45)
print(current_time)     # 16:25:45


#date
import datetime

yesterday = datetime.date(2021, 11, 28)
today = datetime.date.today()

print(yesterday, today)
print(f"{today.day}.{today.month}.{today.year}")

from datetime import datetime
 
deadline = datetime(2017, 5, 10)
print(deadline)     # 2017-05-10 00:00:00
 
deadline = datetime(2017, 5, 10, 4, 30)
print(deadline)     # 2017-05-10 04:30:00

now = datetime.now()
print(now)     # 2017-05-03 11:18:56.239443
 
print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 3.5.2017  11:21
 
print(now.date())
print(now.time())

from datetime import datetime
deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00
 
deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00
 
deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00