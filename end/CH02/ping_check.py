import os
command = "ping -c 1 -w 2 127.0.0.1 > /dev/null 2>&1"
response = os.system(command)
if response == 0:
    print("Ping success")
else:
    print("Ping error")
    