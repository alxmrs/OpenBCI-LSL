#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys

# Note we need to import the QtCore
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # We create a push button. The button is an instance of the
        # QtGui.QPushButton class.
        # First param: the constructor is the label of the button.
        # Second param: parent widget.
        # The parent widget is Example widget, which is a QtGui.QWidget
        # by inheritance
        qbtn = QtGui.QPushButton('Quit', self)

        # The event processing system in PyQt4 is built with the signal &
        # slot mechanism. If we click on the button, the signal clicked
        # is emitted. The slot can be a Qt slot or any python callable.
        # The communication is done between two objects: the sender and
        # the receiver. The sender is the push button, the receiver is the
        # application object.
        qbtn.clicked.connect(
            # The QtCore.QCoreApplication contains the main event loop.
            # It processes and displatches all events. The instance()
            # method gives us its current instance. Note that
            # QtCore.QCoreApplication is created with the QtGui.QApplication.
            # The clicked signal is connected to the quit() method which
            # terminates the application.
            QtCore.QCoreApplication.instance().quit
            )
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
