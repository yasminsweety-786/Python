from datetime import datetime, timedelta

today = datetime.now()

future = today + timedelta(days=7)

print("Today:", today)
print("After 7 Days:", future)