import math

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QWidget
from form import Ui_Main
from controller import Controller
import sys


class myWindow(Ui_Main):

    def __init__(self, window):
        self.setupUi(window)
        self.btnUpdate.clicked.connect(self.clickUpdate)
        self.btnMove.clicked.connect(self.clickMove)
        self.btnMoveBasePlus.clicked.connect(self.clickMoveBasePlus)
        self.btnMoveBaseMinus.clicked.connect(self.clickMoveBaseMinus)
        self.btnMoveShoulderPlus.clicked.connect(self.clickMoveShoulderPlus)
        self.btnMoveShoulderMinus.clicked.connect(self.clickMoveShoulderMinus)
        self.btnMoveElbowPlus.clicked.connect(self.clickMoveElbowPlus)
        self.btnMoveElbowMinus.clicked.connect(self.clickMoveElbowMinus)
        self.btnMoveWrist1Plus.clicked.connect(self.clickMoveWrist1Plus)
        self.btnMoveWrist1Minus.clicked.connect(self.clickMoveWrist1Minus)
        self.btnMoveWrist2Plus.clicked.connect(self.clickMoveWrist2Plus)
        self.btnMoveWrist2Minus.clicked.connect(self.clickMoveWrist2Minus)
        self.btnMoveWrist3Plus.clicked.connect(self.clickMoveWrist3Plus)
        self.btnMoveWrist3Minus.clicked.connect(self.clickMoveWrist3Minus)
        self.btnDigInp0On.clicked.connect(self.clickDigInp0On)
        self.btnDigInp0Off.clicked.connect(self.clickDigInp0Off)
        self.btnDigInp1On.clicked.connect(self.clickDigInp1On)
        self.btnDigInp1Off.clicked.connect(self.clickDigInp1Off)
        self.btnDigOut0On.clicked.connect(self.clickDigOut0On)
        self.btnDigOut0Off.clicked.connect(self.clickDigOut0Off)
        self.btnDigOut1On.clicked.connect(self.clickDigOut1On)
        self.btnDigOut1Off.clicked.connect(self.clickDigOut1Off)
        self.controller = Controller()

    def clickUpdate(self):
        result = self.controller.update(ui)
        res = isinstance(result, str)
        if res==True:
            test = "test"
        else:
            ui.txtX.setText(result["X"])
            ui.txtY.setText(result["Y"])
            ui.txtZ.setText(result["Y"])
            ui.txtRX.setText(result["RX"])
            ui.txtRY.setText(result["RY"])
            ui.txtRZ.setText(result["RZ"])
            ui.txtBase.setText(result["base"])
            ui.txtShoulder.setText(result["shoulder"])
            ui.txtElbow.setText(result["elbow"])
            ui.txtWrist1.setText(result["wrist1"])
            ui.txtWrist2.setText(result["wrist2"])
            ui.txtWrist3.setText(result["wrist3"])

    def clickMove(self):
        basemove = str(ui.txtBase.text())
        shouldermove = str(ui.txtShoulder.text())
        elbowmove = str(ui.txtElbow.text())
        wrist1move = str(ui.txtWrist1.text())
        wrist2move = str(ui.txtWrist2.text())
        wrist3move = str(ui.txtWrist3.text())
        self.controller.sendMoveCommand(ui, basemove, shouldermove, elbowmove, wrist1move, wrist2move, wrist3move, "")

    def clickMoveBasePlus(self):
        basemove = ui.txtBase.text()
        basemove = float(basemove) + 2
        ui.txtBase.setText(str(basemove))
        self.clickMove()

    def clickMoveBaseMinus(self):
        basemove = ui.txtBase.text()
        basemove = float(basemove) - 2
        ui.txtBase.setText(str(basemove))
        self.clickMove()

    def clickMoveShoulderPlus(self):
        shouldermove = ui.txtShoulder.text()
        shouldermove = float(shouldermove) + 2
        ui.txtShoulder.setText(str(shouldermove))
        self.clickMove()

    def clickMoveShoulderMinus(self):
        shouldermove = ui.txtShoulder.text()
        shouldermove = float(shouldermove) - 2
        ui.txtShoulder.setText(str(shouldermove))
        self.clickMove()

    def clickMoveElbowPlus(self):
        elbowmove = ui.txtElbow.text()
        elbowmove = float(elbowmove) + 2
        ui.txtElbow.setText(str(elbowmove))
        self.clickMove()

    def clickMoveElbowMinus(self):
        elbowmove = ui.txtElbow.text()
        elbowmove = float(elbowmove) - 2
        ui.txtElbow.setText(str(elbowmove))
        self.clickMove()

    def clickMoveWrist1Plus(self):
        wrist1move = ui.txtWrist1.text()
        wrist1move = float(wrist1move) + 2
        ui.txtWrist1.setText(str(wrist1move))
        self.clickMove()

    def clickMoveWrist1Minus(self):
        wrist1move = ui.txtWrist1.text()
        wrist1move = float(wrist1move) - 2
        ui.txtWrist1.setText(str(wrist1move))
        self.clickMove()

    def clickMoveWrist2Plus(self):
        wrist2move = ui.txtWrist2.text()
        wrist2move = float(wrist2move) + 2
        ui.txtWrist2.setText(str(wrist2move))
        self.clickMove()

    def clickMoveWrist2Minus(self):
        wrist2move = ui.txtWrist2.text()
        wrist2move = float(wrist2move) - 2
        ui.txtWrist2.setText(str(wrist2move))
        self.clickMove()

    def clickMoveWrist3Plus(self):
        wrist3move = ui.txtWrist3.text()
        wrist3move = float(wrist3move) + 2
        ui.txtWrist3.setText(str(wrist3move))
        self.clickMove()

    def clickMoveWrist3Minus(self):
        wrist3move = ui.txtWrist3.text()
        wrist3move = float(wrist3move) - 2
        ui.txtWrist3.setText(str(wrist3move))
        self.clickMove()

    def clickDigInp0On(self):
        commandTxt = "set_tool_digital_in(0, True)"
        self.clickSendCommand(commandTxt)

    def clickDigInp0Off(self):
        commandTxt = "set_tool_digital_in(0, False)"
        self.clickSendCommand(commandTxt)

    def clickDigInp1On(self):
        commandTxt = "set_tool_digital_in(1, True)"
        self.clickSendCommand(commandTxt)

    def clickDigInp1Off(self):
        commandTxt = "set_tool_digital_in(1, False)"
        self.clickSendCommand(commandTxt)

    def clickDigOut0On(self):
        commandTxt = "set_tool_digital_out(0, True)"
        self.clickSendCommand(commandTxt)

    def clickDigOut0Off(self):
        commandTxt = "set_tool_digital_out(0, False)"
        self.clickSendCommand(commandTxt)

    def clickDigOut1On(self):
        commandTxt = "set_tool_digital_out(1, True)"
        self.clickSendCommand(commandTxt)

    def clickDigOut1Off(self):
        commandTxt = "set_tool_digital_out(1, False)"
        self.clickSendCommand(commandTxt)

    def clickSendCommand(self, commandTxt):
        self.controller.sendCommand(ui, commandTxt)

    def showError(self, title, errormsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errormsg)
        msg.setWindowTitle(title)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = myWindow(MainWindow)
    MainWindow.show()
    app.exec_()
