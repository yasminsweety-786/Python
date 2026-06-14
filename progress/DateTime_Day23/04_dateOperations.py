from datetime import datetime

date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 1, 10)

difference = date2 - date1

print(difference.days)