#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This example shows a tooltip on
a window and a button

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

        # This static method sets a font used to render tooltips.
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        # To create the tooltip, we call the setTooltip() method. We
        # can also use rich text formatting.
        self.setToolTip('This is a <b>QWidget</b> widget')

        #We create a button widget and set the tooltip for it.
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # This button is being resized and moved on the window. The
        # sizeHint() method gives a recommended size for the button.
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()