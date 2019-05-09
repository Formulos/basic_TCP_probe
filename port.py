"""
The code available at https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
was used has a base for this one.
"""


import socket
import subprocess
import sys
import time

def tcp_probe():
    # Ask for input

    remoteServer    = (input("Enter the ip or the host name to begin scan (leave empty for localhost): ") or "localhost")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    low = int(input("Start port (leave empty for the default 1): ") or 1)
    cel = int(input("End port (leave empty for the default 65534): ") or 65534)

    socket.setdefaulttimeout(0.1)

    # Print a nice banner with information on which host we are about to scan
    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60)

    # Check what time the scan started
    start_time = time.time()
    for port in range(low,cel+1):    
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            
            if result == 0:
                if port in range(1,1025):
                    print("Well know Port: {}  Name: {} Status: Open".format(port,socket.getservbyport(port)))
                else:
                    print ("Port: {}  Name: {} Status: Open".format(port,socket.getservbyport(port)))
            sock.close()


        except socket.gaierror:
            sys.exit('Hostname could not be resolved. Exiting')

        except:
            continue

    # Checking the time again
    end_time = time.time()


    # Printing the information to screen
    print ('Scanning Completed in: ', end_time-start_time, " seconds")


tcp_probe()