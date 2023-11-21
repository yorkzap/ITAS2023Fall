from datetime import datetime

today = datetime.now()
print(today)

current_time = today.strftime('%H:%M:%S')
print(today.strftime('%m'))