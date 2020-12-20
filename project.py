#print("hello")
#print ("welcome to KO")

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'nu.edu.com'
#nu.edu used as an example

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,1000):
    if pscan(x):
        print('Port',x,'is open')

sys.stdout = open('log.txt', 'w')
print ('write to this file ')






