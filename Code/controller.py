import sys
import socket
import time
import math
from struct import *


class Controller():

    def update(self, ui):
        try:
            result = {"X": "0", "Y": "0", "Z": "0", "RX": "0", "RY": "0", "RZ": "0"}
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = socket.gethostbyname("192.168.99.128")
            port = 30001
            address = (ip, port)
            client.connect(address)
            time.sleep(0.5)
            boolTrue = True
            while boolTrue == True:
                data = client.recv(1024)
                # print (data)
                packlen = (unpack('!i', data[0:4]))[0]
                #print('packet length: ' + str(packlen))
                packtype = (unpack('!B', data[4:5]))[0]
                #print('packet type: ' + str(packtype))
                i = 0
                if packtype == 16:
                    #print("16 hit")
                    while i + 5 < packlen:

                        # extract length and type of message and print if desired
                        msglen = (unpack('!i', data[5 + i:9 + i]))[0]
                        msgtype = (unpack('!b', data[9 + i:10 + i]))[0]
                        #print('message length: ' + str(msglen))
                        #print('message type: ' + str(msgtype))

                        if msgtype == 1:
                            # if message is joint data, create a list to store angles
                            angle = [0] * 6
                            grad = [0] * 6
                            j = 0
                            while j < 6:
                                # cycle through joints and extract only current joint angle (double precision)  then print to screen
                                # bytes 10 to 18 contain the j0 angle, each joint's data is 41 bytes long (so we skip j*41 each time)
                                angle[j] = (unpack('!d', data[10 + i + (j * 41):18 + i + (j * 41)]))[0]
                                grad[j] = round(((angle[j] * 180) / math.pi), 2)
                                #print('Joint ' + str(j) + ' angle : ' + str(angle[j]) + ' grad: ' + str(grad[j]))
                                j = j + 1
                            result["base"] = str(grad[0])
                            result["shoulder"] = str(grad[1])
                            result["elbow"] = str(grad[2])
                            result["wrist1"] = str(grad[3])
                            result["wrist2"] = str(grad[4])
                            result["wrist3"] = str(grad[5])



                        elif msgtype == 4:
                            # if message type is cartesian data, extract doubles for 6DOF pos of TCP and print to sc    reen
                            x = (unpack('!d', data[10 + i:18 + i]))[0]
                            y = (unpack('!d', data[18 + i:26 + i]))[0]
                            z = (unpack('!d', data[26 + i:34 + i]))[0]
                            rx = (unpack('!d', data[34 + i:42 + i]))[0]
                            ry = (unpack('!d', data[42 + i:50 + i]))[0]
                            rz = (unpack('!d', data[50 + i:58 + i]))[0]

                            result["X"] = str(round((x * 1000), 2))
                            result["Y"] = str(round((y * 1000), 2))
                            result["Z"] = str(round((z * 1000), 2))
                            result["RX"] = str(round(rx, 3))
                            result["RY"] = str(round(ry, 3))
                            result["RZ"] = str(round(rz, 3))
                            boolTrue = False
                        i = msglen + i
        except Exception as e:
            ui.showError("Error", str(e))
        return result

    def sendCommand(self, ui, commandTxt):
        result = ""
        try:
            host = "192.168.99.128"
            port = 30002

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            cmd = commandTxt + "\n"
            s.send(cmd.encode('utf-8'))

            data = s.recv(1024)
            s.close()
            result = data
        except Exception as e:
            ui.showError("Error", str(e))
        return result

    def sendMoveCommand(self, ui, basemove, shouldermove, elbowmove, wrist1move, wrist2move, wrist3move, pstr):
        result = ""
        try:
            host = "192.168.99.128"
            port = 30001
            #print('The computer is connecet to ' + str(HOST) + ' on port ' + str(PORT))

            time.sleep(0.5)
            #print('attemt to send data via socket')

            basemove = float(basemove)
            realBasemove = (basemove * (math.pi / 180.0))
            realBasemove = str(realBasemove)

            shouldermove = float(shouldermove)
            realShouldermove = (shouldermove * (math.pi / 180.0))
            realShouldermove = str(realShouldermove)

            elbowmove = float(elbowmove)
            realElbowmove = (elbowmove * (math.pi / 180.0))
            realElbowmove = str(realElbowmove)

            wrist1move = float(wrist1move)
            realWrist1move = (wrist1move * (math.pi / 180.0))
            realWrist1move = str(realWrist1move)

            wrist2move = float(wrist2move)
            realWrist2move = (wrist2move * (math.pi / 180.0))
            realWrist2move = str(realWrist2move)

            wrist3move = float(wrist3move)
            realWrist3move = (wrist3move * (math.pi / 180.0))
            realWrist3move = str(realWrist3move)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            time.sleep(0.5)

            #print("Moving robot to new positions based on it's joint positions")

            move = "movej("+pstr+"[0" + realBasemove + ", 0" + realShouldermove + ", 0" + realElbowmove + ", 0" + realWrist1move + ", 0" + realWrist2move + ", 0" + realWrist3move + "],a=1.0," "v=0.1)" + "\n"

            ## if we need more difrens point to move to

            # move2 = "movej([0, 0, 0, 0, 0, 0], a=1.0, v=0.1)" + "\n"
            # move3 = "movej([-1.96, -1.53, 2.08, -2.12, -1.56, 1.19], a=1.0, v=0.1)" + "\n"

            s.send(move.encode('utf-8'))
            time.sleep(1)

            data = s.recv(1024)
            s.close()
            result = data
        except Exception as e:
            ui.showError("Error", str(e))
        return result