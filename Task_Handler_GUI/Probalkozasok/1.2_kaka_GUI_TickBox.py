import sys
import re
from PyQt4 import QtGui, QtCore

string = []
regex_words = ''
class Window(QtGui.QMainWindow): 

    def __init__(self):
        super(Window, self).__init__() ##superrel atadjuk a parent objektet -->QMainWindow -ot
        self.setGeometry(550, 500, 700, 500) #itt lehet hivatkozni a window-ra mint sajat maga -->self-->window
        self.setWindowTitle("")
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
        btn = QtGui.QPushButton("Kereses" ,self)#ez legyen a neve aztan kuldje el a Window-ot
        btn.clicked.connect(self.searching) #Connect megmondja, mit csinaljon a gomb, ha raboknek
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(200,200)

        checkBox = QtGui.QCheckBox('Base +',self)
        checkBox.move(0,15)
        checkBox.stateChanged.connect(self.tick_1)

        checkBox = QtGui.QCheckBox('Base -',self)
        checkBox.move(60,15)
        checkBox.stateChanged.connect(self.tick_2)

        checkBox = QtGui.QCheckBox('Regession',self)
        checkBox.move(0,35)
        checkBox.stateChanged.connect(self.tick_3)

        checkBox = QtGui.QCheckBox('ToDo',self)
        checkBox.move(70,35)
        checkBox.stateChanged.connect(self.tick_4)

        checkBox = QtGui.QCheckBox('Automat',self)
        checkBox.move(0,55)
        checkBox.stateChanged.connect(self.tick_5)

        checkBox = QtGui.QCheckBox('ActiveDischarge',self)
        checkBox.move(200,15)
        checkBox.stateChanged.connect(self.tick_6)

        checkBox = QtGui.QCheckBox('ModeManager',self)
        checkBox.move(310,15)
        checkBox.stateChanged.connect(self.tick_7)

        checkBox = QtGui.QCheckBox('Offset',self)
        checkBox.move(400,15)
        checkBox.stateChanged.connect(self.tick_8)
        self.show() 

    # Back End
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

    def tick_3(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Regession' +')')            
         else:
            string.remove('(?=.*#'+ 'Regession' +')')
    def tick_4(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ToDo' +')')            
         else:
            string.remove('(?=.*#'+ 'ToDo' +')')
            

    def tick_5(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Automat' +')')            
         else:
            string.remove('(?=.*#'+ 'Automat' +')')

    def tick_6(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ActiveDischarge' +')')            
         else:
            string.remove('(?=.*#'+ 'ActiveDischarge' +')')

    def tick_7(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ModeManager' +')')            
         else:
            string.remove('(?=.*#'+ 'ModeManager' +')')

    def tick_8(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Offset' +')')            
         else:
            string.remove('(?=.*#'+ 'Offset' +')')



    def close_application(self):
        print('kileptel yoyo')
        sys.exit()

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
                print(megVagy, end='' )

            print()
            print('----------------------------------oo------------------------------------')


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()



#CANape CANoe ECUtest Git Polarion ToDo Automat
#Review  Offset  ModeManager Defect Meeting KnowHow Xlsx Regession Trace MiniHIL
#Letter Jenkins Link AddWorkFlow BaseMinus Directiva BasePlus