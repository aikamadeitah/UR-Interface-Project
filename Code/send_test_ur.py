import socket
import time

HOST = "192.168.99.128"
PORT = 30002
print ('The computer is connecet to ' + str(HOST) + ' on port ' + str(PORT))

time.sleep(1)
print('attemt to send data via socket')

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = "set_payload_mass(2.0)" + "\n"
s.send(cmd.encode('utf-8'))

data = s.recv(1024)
s.close()

print ('Recived', repr(data))