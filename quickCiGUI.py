from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import gui

class QuickCI(QtWidgets.QMainWindow, gui.Ui_Dialog):
    def __init__(self, parent=None):
        super(QuickCI, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = QuickCI()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()