#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This program centers a window
on the screen.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui

# The QtGui.QDesktopWidget class provides information about the user's
# desktop, including the screen size.

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()           # Custom center method

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # we get a rectangle specifying hte geometry of the main window.
        # This includes any window frame
        qr = self.frameGeometry()
        # We figure out the screen resolution of our monitor. From this
        # we get the center point.
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        # Our rectangle has already its width and height. Now we sent the
        # center of the rectangle to the center of the screen. The rect's
        # size is unchanged.
        qr.moveCenter(cp)
        # We move the top-left point of the application window to the
        # top-left point of the qr rectangle, thus centering the window on
        # our screen.
        self.move(qr.topLeft())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()