import sys ,re
from PyQt4 import QtGui ,QtCore

string = []
regex_words = ''
finding = []
urit = []
txt_path = []

class Window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.setGeometry(100, 100, 1700, 800)
        self.setWindowTitle("DataBase for HashTagging")

        self.setStyleSheet('font-size: 9pt; font-family: Europa;')

       


      
        self.button = QtGui.QPushButton('EXIT')

        self.textedit = QtGui.QTextEdit()
        self.textedit.setReadOnly(True)
        self.textedit.setFontPointSize(12)
        layout.addWidget(self.textedit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.close_application)

        
        offset = 500

        btn = QtGui.QPushButton("Search" ,self)
        btn.clicked.connect(self.searching)
        btn.resize(100,80)
        btn.move(offset + 700,500)

        btn = QtGui.QPushButton("Clear" ,self)
        btn.clicked.connect(self.empty_array)
        btn.resize(100,80)
        #btn.resize(btn.minimumSizeHint())
        btn.move(offset + 800,500)


        btn = QtGui.QPushButton("Open TXT" ,self)
        btn.clicked.connect(self.file_open)
        btn.resize(150,80)
        #btn.resize(btn.minimumSizeHint())
        btn.move(offset + 1030,660)          



        # Projects 2 db
        project_y = 50
        checkBox = QtGui.QCheckBox('Base +',self)
        checkBox.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}")
        checkBox.move(offset + 700,project_y)
        checkBox.stateChanged.connect(self.tick_1)

        checkBox = QtGui.QCheckBox('Base -',self)
        checkBox.move(offset + 780,project_y)
        checkBox.stateChanged.connect(self.tick_2)
        # Tools
        tool_y = 380
        checkBox = QtGui.QCheckBox('CANape',self)
        checkBox.resize(btn.sizeHint())
        checkBox.move(offset + 700,tool_y)
        checkBox.stateChanged.connect(self.tick_3)

        checkBox = QtGui.QCheckBox('CANoe',self)
        checkBox.move(offset + 780,tool_y)
        checkBox.stateChanged.connect(self.tick_4)

        checkBox = QtGui.QCheckBox('ECUtest',self)
        checkBox.move(offset + 850,tool_y)
        checkBox.stateChanged.connect(self.tick_5)

        checkBox = QtGui.QCheckBox('Trace',self)
        checkBox.move(offset + 930,tool_y)
        checkBox.stateChanged.connect(self.tick_6)

        # Infrastructs
        infrastuct_y = 210

        checkBox = QtGui.QCheckBox('Git',self)
        checkBox.move(offset + 700,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_7)

        checkBox = QtGui.QCheckBox('Polarion',self)
        checkBox.move(offset + 745,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_8)

        checkBox = QtGui.QCheckBox('Jenkins',self)
        checkBox.move(offset + 820,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_9)

        checkBox = QtGui.QCheckBox('MiniHIL',self)
        checkBox.move(offset + 890,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_10)
        # Topics
        topics_y = 90
        checkBox = QtGui.QCheckBox('Offset',self)
        checkBox.move(offset + 700,topics_y)
        checkBox.stateChanged.connect(self.tick_11)

        checkBox = QtGui.QCheckBox('ModeManager',self)
        checkBox.move(offset + 780,topics_y)
        checkBox.stateChanged.connect(self.tick_12)

        checkBox = QtGui.QCheckBox('ActiveDischarge',self)
        checkBox.move(offset + 900,topics_y)
        checkBox.stateChanged.connect(self.tick_13)

        # Works
        work_y = 130
        checkBox = QtGui.QCheckBox('ToDo',self)
        checkBox.move(offset + 700,work_y)
        checkBox.stateChanged.connect(self.tick_14)

        checkBox = QtGui.QCheckBox('Defect',self)
        checkBox.move(offset + 760,work_y)
        checkBox.stateChanged.connect(self.tick_15)

        checkBox = QtGui.QCheckBox('Automat',self)
        checkBox.move(offset + 830,work_y)
        checkBox.stateChanged.connect(self.tick_16)

        checkBox = QtGui.QCheckBox('Meeting',self)
        checkBox.move(offset + 910,work_y)
        checkBox.stateChanged.connect(self.tick_17)

        checkBox = QtGui.QCheckBox('Regession',self)
        checkBox.move(offset + 990,work_y)
        checkBox.stateChanged.connect(self.tick_18)

        checkBox = QtGui.QCheckBox('Review',self)
        checkBox.move(offset + 1090,work_y)
        checkBox.stateChanged.connect(self.tick_19)


        #Miscs
        misc_y = 300
        checkBox = QtGui.QCheckBox('AddWorkFlow',self)
        checkBox.move(offset + 700,misc_y)
        checkBox.stateChanged.connect(self.tick_20)

        checkBox = QtGui.QCheckBox('KnowHow',self)
        checkBox.move(offset + 820,misc_y)
        checkBox.stateChanged.connect(self.tick_21)

        checkBox = QtGui.QCheckBox('Directiva',self)
        checkBox.move(offset + 920,misc_y)
        checkBox.stateChanged.connect(self.tick_22)

        checkBox = QtGui.QCheckBox('Xlsx',self)
        checkBox.move(offset + 1010,misc_y)
        checkBox.stateChanged.connect(self.tick_23)

        checkBox = QtGui.QCheckBox('Letter',self)
        checkBox.move(offset + 1070,misc_y)
        checkBox.stateChanged.connect(self.tick_24)

        checkBox = QtGui.QCheckBox('Link',self)
        checkBox.move(offset + 1100,misc_y)
        checkBox.stateChanged.connect(self.tick_25)



        

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
            string.append('(?=.*#'+ 'CANape' +')')            
         else:
            string.remove('(?=.*#'+ 'CANape' +')')            
    def tick_4(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'CANoe' +')')            
        else:
            string.remove('(?=.*#'+ 'CANoe' +')')
    def tick_5(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ECUtest' +')')            
         else:
            string.remove('(?=.*#'+ 'ECUtest' +')')            
    def tick_6(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Trace' +')')            
        else:
            string.remove('(?=.*#'+ 'Trace' +')')
    def tick_7(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Git' +')')            
         else:
            string.remove('(?=.*#'+ 'Git' +')')            
    def tick_8(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Polarion' +')')            
        else:
            string.remove('(?=.*#'+ 'Polarion' +')')
    def tick_9(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Jenkins' +')')            
         else:
            string.remove('(?=.*#'+ 'Jenkins' +')')            
    def tick_10(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'MiniHIL' +')')            
        else:
            string.remove('(?=.*#'+ 'MiniHIL' +')')
    def tick_11(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Offset' +')')            
        else:
            string.remove('(?=.*#'+ 'Offset' +')')
    def tick_12(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ModeManager' +')')            
        else:
            string.remove('(?=.*#'+ 'ModeManager' +')')
    def tick_13(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ActiveDischarge' +')')            
        else:
            string.remove('(?=.*#'+ 'ActiveDischarge' +')')
    def tick_14(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ToDo' +')')            
        else:
            string.remove('(?=.*#'+ 'ToDo' +')')
    def tick_15(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Defect' +')')            
        else:
            string.remove('(?=.*#'+ 'Defect' +')')
    def tick_16(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Automat' +')')            
        else:
            string.remove('(?=.*#'+ 'Automat' +')')
    def tick_17(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Meeting' +')')            
        else:
            string.remove('(?=.*#'+ 'Meeting' +')')
    def tick_18(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Regession' +')')            
        else:
            string.remove('(?=.*#'+ 'Regession' +')')    
    def tick_19(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Review' +')')            
        else:
            string.remove('(?=.*#'+ 'Review' +')')
    def tick_20(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'AddWorkFlow' +')')            
        else:
            string.remove('(?=.*#'+ 'AddWorkFlow' +')')
    def tick_21(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'KnowHow' +')')            
        else:
            string.remove('(?=.*#'+ 'KnowHow' +')')
    def tick_22(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Directiva' +')')            
        else:
            string.remove('(?=.*#'+ 'Directiva' +')')
    def tick_23(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Xlsx' +')')            
        else:
            string.remove('(?=.*#'+ 'Xlsx' +')')
    def tick_24(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Letter' +')')            
        else:
            string.remove('(?=.*#'+ 'Letter' +')')
    def tick_25(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Link' +')')            
        else:
            string.remove('(?=.*#'+ 'Link' +')')

    def print_out(self):

        self.empty_array()
        self.textedit.append(" ")
        finding_ = "".join(str(x) for x in finding)

        self.textedit.append(finding_)
        self.init()
        

        #finding_ = "".join(str(x) for x in urit)

    def empty_array(self):
        self.textedit.clear()

    def close_application(self):
        print('kileptel yoyo')
        sys.exit()

    def file_open(self):
        del txt_path[:]
        txt_path.append(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        #print(txt_path)
        print(txt_path[0])
       #file = open(name , 'r')
        

    def init(self):
        del finding[:]

    def searching(self):
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        regex_words = "".join(str(x) for x in string)
        kulcsSzo = r"(?=.*)" + regex_words
        kaka = txt_path[0]
        
             
        #print(kulcsSzo)
        #self.init()
        #self.empty_array()
        ending = '\\+'
        pattern_keyword = re.compile( kulcsSzo )
        pattern_end = re.compile( ending )
        

        # Loop through text
        for i, line in enumerate(open(kaka)):
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
            finding.append('''------------------------------------------------------------------------------------------------------------------------''' + '\n')

            for lezaro in sorban_end[0:len(sorban_end)]:
                if hits < lezaro:
                    #print(hits)
                    #print(lezaro)
                    break

            for megVagy in text[hits-1:lezaro-1]:
                finding.append( megVagy )

            

            
        print('----------------------------------oo------------------------------------')
        self.print_out()
        

    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    k=input("press close to exit") 


#Hetfo Kedd Szerda Csutortok Pentek  
#BaseMinus BasePlus
#CANape CANoe ECUtest Trace Git Polarion Jenkins MiniHIL
#ToDo Defect Meeting
#Review  Regession
#Offset  ModeManager ActiveDischarge Automat
#AddWorkFlow KnowHow Directiva
#   Xlsx   
#Letter  Link    