import os
command = "ping -c 1 -w 2 127.0.0.1 > /dev/null 2>&1"
result = os.system(command)
if result == 0:
    print("Ping successful!")
else:
    print("Ping failed!")
    