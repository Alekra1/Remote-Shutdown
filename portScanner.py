import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = "100.117.46.24"

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

flag = 0;

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, 8080))
    if result == 0:
        print("Port {} is open".format("8080"))
    else :
        print("Port {} is closed".format("8080"))
    # for port in range(1, 100):
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     socket.setdefaulttimeout(1)
    #
    #     result = s.connect_ex((target, port))
    #     if result == 0:
    #         flag = 1;
    #         print("Port {} is open".format(port))
    #     else :
    #         print("Port {} is closed".format(port))
    #     s.close()
    # if flag == 0:
    #         print("no ports are open")


except KeyboardInterrupt:
    print("\n Exitting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
