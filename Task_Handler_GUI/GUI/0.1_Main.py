import sys
from PyQt4 import QtGui, QtCore
#Event is lehessen a gombra

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__() ##superrel atadjuk a parent objektet -->QMainWindow -ot
        self.setGeometry(50, 50, 500, 300) #itt lehet hivatkozni a window-ra mint sajat maga -->self-->window
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pyLogo.png'))


        extractAcction = QtGui.QAction("&Kilepek",self)
        extractAcction.setShortcut("Ctrl+Q")
        extractAcction.setStatusTip("Leave the App")
        extractAcction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar() #azert add neki valtozot mert ezt valtoztatni fogjuk nem ugy mint a statusbar
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAcction)


        self.home()
        
    def home(self):
    	btn = QtGui.QPushButton("Quit" ,self)
    	btn.clicked.connect(self.close_application)
    	btn.resize(btn.sizeHint())
    	btn.resize(btn.minimumSizeHint())
    	btn.move(100,100)    	
    	self.show()

    def close_application(self):
        print('jaja jo lesz ez, kileptel yoyo') 
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
