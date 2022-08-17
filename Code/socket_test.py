import sys
import socket   
import time
import math
from struct import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
ip=socket.gethostbyname("192.168.99.128")
port=30001
address=(ip,port)
client.connect(address)
#print int(address)
print ('The computer is connecet to ' + str(ip) + ' on port ' + str(port))

time.sleep(1)
print('attemt to get data from socket')


while True:
    data = client.recv(1024)
    #print (data)
    packlen =  (unpack('!i', data[0:4]))[0]
    print ('packet length: ' + str(packlen))
    packtype = (unpack('!B', data[4:5]))[0]
    print ('packet type: ' + str(packtype))
    i = 0
    if packtype == 16:
        print("16 hit")
        while i+5 < packlen:

            #extract length and type of message and print if desired
            msglen = (unpack('!i', data[5+i:9+i]))[0] 
            msgtype = (unpack('!b', data[9+i:10+i]))[0] 
            print ('message length: ' + str(msglen))
            print ('message type: ' + str(msgtype))
            
            if msgtype == 1:
                #if message is joint data, create a list to store angles
                angle = [0]*6
                grad = [0]*6
                j = 0
                while j < 6:
                    #cycle through joints and extract only current joint angle (double precision)  then print to screen
                    #bytes 10 to 18 contain the j0 angle, each joint's data is 41 bytes long (so we skip j*41 each time)
                    angle[j] = (unpack('!d', data[10+i+(j*41):18+i+(j*41)]))[0]
                    grad[j]=round(((angle[j]*180)/math.pi), 2)
                    print ('Joint ' + str(j) + ' angle : ' + str(angle[j]) + ' grad: '+str(grad[j]))
                    j = j + 1
                     
                print ('*******')

            elif msgtype == 4:
                #if message type is cartesian data, extract doubles for 6DOF pos of TCP and print to sc    reen
                x =  (unpack('!d', data[10+i:18+i]))[0]
                y =  (unpack('!d', data[18+i:26+i]))[0]
                z =  (unpack('!d', data[26+i:34+i]))[0]
                rx =  (unpack('!d', data[34+i:42+i]))[0]
                ry =  (unpack('!d', data[42+i:50+i]))[0]
                rz =  (unpack('!d', data[50+i:58+i]))[0]

                #print ('X:  ' + str(((x*180)/math.pi)/57300))
                print ('X:  ' + str(round((x*1000),2)))
                print ('Y:  ' + str(round((y*1000),2)))
                print ('Z:  ' + str(round((z*1000),2)))
                print ('RX: ' + str(round(rx,3)))
                print ('RY: ' + str(round(ry,3)))
                print ('RZ: ' + str(round(rz,3)))
                print ('*******\n')
            
            i = msglen + i
    
    
    
    
    #timestamp = (unpack('!Q', data[10:18]))[0]
    #print ('timestamp: ' + str(timestamp))
    #packlen =  (unpack('!i', data[0:4]))[0]
    #print(packlen)
    #packtype = (unpack('!b', data[4]))[0] 
    #print(
    sys.stdout.flush()
    #packsize=messageSize
    #print(packsize)
    #exit()
    #string = str(data.decode())
    #print(string)
