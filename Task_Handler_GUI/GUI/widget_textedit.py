import sys ,re
from PyQt4 import QtGui ,QtCore
from functools import partial

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        title = QtGui.QPushButton( 'Title' )
        author = QtGui.QPushButton( 'Author' )
        other = QtGui.QPushButton( 'Other' )

        titleEdit = QtGui.QTextEdit()

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget( title )
        horizontalLayout.addWidget( author )
        horizontalLayout.addWidget( other )

        verticalLayout = QtGui.QVBoxLayout( self )
        verticalLayout.addLayout( horizontalLayout )

        verticalLayout.addWidget( titleEdit )


        self.setLayout( verticalLayout )

        self.setGeometry( 300, 300, 350, 300 )
        self.setWindowTitle( 'Review' )
        self.show()

def main():

    app = QtGui.QApplication( sys.argv )
    ex = Example()
    sys.exit( app.exec_() )


if __name__ == '__main__':
    main()