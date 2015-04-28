"""
ZetCode PyQt4 tutorial

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui

# Class inherits from QtGui.QWidget class. This means we call two
# constructors: the first one for the Example class and the second
# one for the inherited class.
class Example(QtGui.QWidget):

    # The super() method returns the parent object of the Example
    # class and we call its constructor the __init__() method is a
    # constructor method in Python
    def __init__(self):
        super(Example, self).__init__()

        # creation of the GUI is delegated to the initUI() method
        self.initUI()

    # All three methods called are inherited from the QtGui.QWidget
    # class.
    def initUI(self):
        # Locates the windown on the screen and sets its size
        # (x_pos, y_pos, width, height).
        # This combines resize() and move() in one method.
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')                 # Set window title
        # Set Sets application icon. To do this, it creates a
        # QtGui.QIcon obect. The QtGui.QIcon receives the path to be
        # displayed.
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show() # Show the UI

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()