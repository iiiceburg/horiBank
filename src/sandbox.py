from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
dt_object = datetime.fromtimestamp(timestamp)

print("timestamp =", dt_object)