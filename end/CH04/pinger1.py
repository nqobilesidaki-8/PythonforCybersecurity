import os
import platform

ip = "127.0.0.1"
command = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

exit_code = os.system(command)
print(exit_code)
