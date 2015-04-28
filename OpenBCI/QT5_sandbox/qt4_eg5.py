#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This program shows a confirmation
message box when we click on the close
button of the application window.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    # If we close a QtGui.QWidget, a QtGui.QCloseEvent is generated.
    # To modify the widget behavior we need to reimplement the
    # closeEvent() event handler.
    def closeEvent(self, event):
        # The first string appears on the titlebar.
        # The second string is the message text displayed by the dialog.
        # The third arg specifies the combination of buttons appearing
        # in the dialog.
        # The last param is the default button, the button which has
        # initially the keyboard focus.
        # The return value is stores in the reply var.
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        # Here we test the return value. If we click Yes, we accept which
        # leads to teh closure of the widget and termination of the
        # application. Otherwise we close the event.
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()