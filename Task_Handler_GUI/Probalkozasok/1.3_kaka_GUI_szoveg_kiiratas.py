import sys
import re
from PyQt4 import QtGui, QtCore

string = []
regex_words = ''
finding = ''

class Window(QtGui.QMainWindow): 

    def __init__(self):
        super(Window, self).__init__() 
        self.setGeometry(550, 500, 700, 500) 
        self.setWindowTitle("Hash Tagging")
        self.setWindowIcon(QtGui.QIcon('pyLogo.png'))

        extractAcction = QtGui.QAction("&Kilepek",self)
        extractAcction.setShortcut("Ctrl+Q")
        extractAcction.setStatusTip("Leave the App")
        extractAcction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAcction)
        self.home()

    def home(self):

    	self.button = QtGui.QPushButton('button')
    	layout = QtGui.QVBoxLayout(self)
    	
    	self.textedit = QtGui.QTextEdit()
    	self.textedit.setReadOnly(True)
    	layout.addWidget(self.textedit)
    	layout.addWidget(self.button)
    	self.button.clicked.connect(self.searching)

    	btn = QtGui.QPushButton("Kereses" ,self)
    	btn.clicked.connect(self.searching)
    	btn.resize(btn.sizeHint())
    	btn.resize(btn.minimumSizeHint())
    	btn.move(200,200)

    	btn = QtGui.QPushButton("Quit", self)
    	btn.clicked.connect(self.close_application)
    	btn.resize(btn.minimumSizeHint())
    	btn.move(0,100)

    	extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Fne', self)
    	extractAction.triggered.connect(self.close_application)
    	self.toolBar = self.addToolBar("Extraction")
    	self.toolBar.addAction(extractAction)
    	checkBox = QtGui.QCheckBox('Base +',self)
    	checkBox.move(0,15)
    	checkBox.stateChanged.connect(self.tick_1)
    	checkBox = QtGui.QCheckBox('Base -',self)
    	checkBox.move(60,15)
    	checkBox.stateChanged.connect(self.tick_2)

    	self.show()
    def tick_1(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'BasePlus' +')')            
         else:
            string.remove('(?=.*#'+ 'BasePlus' +')')            

    def tick_2(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'BaseMinus' +')')            
         else:
            string.remove('(?=.*#'+ 'BaseMinus' +')')





    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Kilepes','Kilepsz?',
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        

    def searching(self):
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        regex_words = "".join(str(x) for x in string)
        kulcsSzo = r"(?=.*)" + regex_words
       
        #print(kulcsSzo)
       
        ending = '\\+'
        pattern_keyword = re.compile( kulcsSzo )
        pattern_end = re.compile( ending )

        # Loop through text
        for i, line in enumerate(open('log_VW_FEB.txt')):
            text.append(line)
            #Kulcs szo
            for match in re.finditer(pattern_keyword, line):
                kulcs_szo_sora.append( i + 1 ) #talalt sor lementese
                break
            # Kereszt lezarasok keresese
            for match in re.finditer(pattern_end, line):
                sorban_end.append( i + 1 ) #talalt kereszt sor lementese

        # Lezaro kereszt elemek tombjenek hossza
        #hossz = len(sorban_end)
        for hits in kulcs_szo_sora:
            print('Eredeti doksiban ezen sor : %s ' % hits)
            print()

            for lezaro in sorban_end[0:len(sorban_end)]:
                if hits < lezaro:
                    #print(hits)
                    #print(lezaro)
                    break

            for megVagy in text[hits-1:lezaro-1]:
                finding = print(megVagy, end='' )
                

            print()
            print('----------------------------------oo------------------------------------')
    print(finding)

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()



#CANape CANoe ECUtest Git Polarion ToDo Automat
#Review  Offset  ModeManager Defect Meeting KnowHow Xlsx Regession Trace MiniHIL
#Letter Jenkins Link AddWorkFlow BaseMinus Directiva BasePlus