"""
ZetCode PyQt4 tutorial

In this example, we create a simple window in PyQt4

Author: Jan Bodnar
Website: zetcode.com
last edited: October 2011

"""

import sys
from PyQt4 import QtGui  # Location of basic GUI widgets

def main():


    # Every PyQt4 application must create a main application object
    # The application object is located in the QtGui module. The
    # sys.argv parameter is alist of arguments from the command line
    app = QtGui.QApplication(sys.argv)

    # The QtGui.QWidget() widget is the base class of all user interface
    # objects in PyQt4. We provide the default constructor for QtGui.QWidget
    # The default ctor has no parent. A widget with no parent is called a
    # window
    w = QtGui.QWidget()

    w.resize(250, 150)          # resized the widget
    w.move(300,300)             # position from top left corner
    w.setWindowTitle('Simple')  # Title shown in titlebar
    w.show()                    # displays widget on screen

    # Finally, we enter the mainloop of the application. The even handling
    # starts from this point. The mainloop receives events from the window
    # system and dispatches them to the application widgets.
    # The mainloop ends if we call exit() method or the main widget is
    # destroyed. The sys.exit() method ensures a clean exit.
    # Because exec() is a python keyword, exec_() was used instead.
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()