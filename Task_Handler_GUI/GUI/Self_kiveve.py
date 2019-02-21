import sys ,re
from PyQt4 import QtGui ,QtCore
from functools import partial

string = []
regex_words = ''
finding = []
urit = []
txt_path = []

class Window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout(self)
        self.setGeometry(100, 100, 1750, 900)
        self.setWindowTitle("DataBase for HashTagging")

        self.setStyleSheet('font-size: 9.7pt; font-family: Europa;')
      
       	button1 = QtGui.QPushButton('Open File')
       	button2 = QtGui.QPushButton('Search File')

        checkBox_1 = QtGui.QCheckBox('Base +',self)
        checkBox_2 = QtGui.QCheckBox('Base -',self)
        #button1.resize(150,80)
        button = QtGui.QPushButton('EXIT')
        #button1.move(100,100)

        self.textedit = QtGui.QTextEdit()
        self.textedit.setReadOnly(True)
        self.textedit.setFontPointSize(12)

        layout.addWidget(button1)
        layout.addWidget(checkBox_1)
        layout.addWidget(checkBox_2)
        checkBox_1.move(0 + 700,0)
        checkBox_1.stateChanged.connect(lambda state: self.tick(state, word1 = 'BasePlus') )
        layout.addWidget(button2)
        layout.addWidget(self.textedit)
        layout.addWidget(button)
        button.clicked.connect(self.close_application)
        button1.clicked.connect(self.file_open)
        button2.clicked.connect(self.searching)


        # Gombok
        offset = 500
       # btn = QtGui.QPushButton("Search" ,self)
       #btn.clicked.connect(self.searching)
       # btn.resize(100,80)
        #btn.move(offset + 700,660)

       # btn = QtGui.QPushButton("Clear" ,self)
        #btn.clicked.connect(self.empty_array)
       # btn.resize(100,80)
        #btn.resize(btn.minimumSizeHint())
       # btn.move(offset + 800,660)


        #btn = QtGui.QPushButton("Open TXT" ,self)
       # btn.clicked.connect(self.file_open)
       #btn.resize(150,80)
        #btn.resize(btn.minimumSizeHint())
       # btn.move(offset + 1030,660)          


        


        # Projects
        project_y = 70
        checkBox1 = QtGui.QCheckBox('Base +',self)
        #checkBox1.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}")
        checkBox1.move(offset + 700,project_y)
        checkBox1.stateChanged.connect(lambda state: self.tick(state, word1 = 'BasePlus') )

        checkBox = QtGui.QCheckBox('Base -',self)
        checkBox.move(offset + 780,project_y)
        checkBox.stateChanged.connect(lambda state: self.tick(state, word1 = 'BaseMinus') )

        checkBox1 = QtGui.QCheckBox('Software',self)
        #checkBox1.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}")
        checkBox1.move(offset + 860,project_y)
        checkBox1.stateChanged.connect(lambda state: self.tick(state, word1 = 'Software') )

        checkBox = QtGui.QCheckBox('SWChange',self)
        checkBox.move(offset + 950,project_y)
        checkBox.stateChanged.connect(lambda state: self.tick(state, word1 = 'SWChange') )
        
        # Topics
        topics_y = 100
        checkBox = QtGui.QCheckBox('Offset',self)
        checkBox.move(offset + 700,topics_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Offset') )

        checkBox = QtGui.QCheckBox('ModeManager',self)
        checkBox.move(offset + 780,topics_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'ModeManager') )

        checkBox = QtGui.QCheckBox('ActiveDischarge',self)
        checkBox.move(offset + 900,topics_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'ActiveDischarge') )

        checkBox = QtGui.QCheckBox('Automat',self)
        checkBox.move(offset + 1020,topics_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Automat') )

        #    Works
        work_y = 150
        checkBox = QtGui.QCheckBox('Requirment',self)
        checkBox.move(offset + 700,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Requirment') )

        checkBox = QtGui.QCheckBox('Defect',self)
        checkBox.move(offset + 810,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Defect') )        

        checkBox = QtGui.QCheckBox('Meeting',self)
        checkBox.move(offset + 885,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Meeting') )

        checkBox = QtGui.QCheckBox('Regession',self)
        checkBox.move(offset + 970,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Regession') )

        checkBox = QtGui.QCheckBox('Review',self)
        checkBox.move(offset + 1070,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Review') )

        checkBox = QtGui.QCheckBox('Nightly',self)
        checkBox.move(offset + 1150,work_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Nightly') )

        

        #    Miscs
        misc_y = 200
        checkBox = QtGui.QCheckBox('AddWorkFlow',self)
        checkBox.move(offset + 700,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'AddWorkFlow') )

        checkBox = QtGui.QCheckBox('KnowHow',self)
        checkBox.move(offset + 820,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'KnowHow') )

        checkBox = QtGui.QCheckBox('Directiva',self)
        checkBox.move(offset + 920,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Directiva') )

        checkBox = QtGui.QCheckBox('Xlsx',self)
        checkBox.move(offset + 1010,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Xlsx') )

        checkBox = QtGui.QCheckBox('Letter',self)
        checkBox.move(offset + 1070,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )

        checkBox = QtGui.QCheckBox('Link',self)
        checkBox.move(offset + 1140,misc_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )

        # Infrastructs
        infrastuct_y = 300
        checkBox = QtGui.QCheckBox('Git',self)
        checkBox.move(offset + 700,infrastuct_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Git') )

        checkBox = QtGui.QCheckBox('Polarion',self)
        checkBox.move(offset + 750,infrastuct_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Polarion') )

        checkBox = QtGui.QCheckBox('Jenkins',self)
        checkBox.move(offset + 840,infrastuct_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Jenkins') )

        checkBox = QtGui.QCheckBox('MiniHIL',self)
        checkBox.move(offset + 920,infrastuct_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'MiniHIL') )

        # Tools
        tool_y = 380
        checkBox = QtGui.QCheckBox('CANape',self)
        #checkBox.resize(btn.sizeHint())
        checkBox.move(offset + 700,tool_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'CANape') )

        checkBox = QtGui.QCheckBox('CANoe',self)
        checkBox.move(offset + 790,tool_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'CANoe') )

        checkBox = QtGui.QCheckBox('ECUtest',self)
        checkBox.move(offset + 870,tool_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'ECUtest') )

        checkBox = QtGui.QCheckBox('Trace',self)
        checkBox.move(offset + 955,tool_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Trace') )

        # File_releated
        File_y = 460
        checkBox = QtGui.QCheckBox('File',self)
        #checkBox.resize(btn.sizeHint())
        checkBox.move(offset + 700,File_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'File') )

        checkBox = QtGui.QCheckBox('Xlsx',self)
        checkBox.move(offset + 760,File_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Xlsx') )

        checkBox = QtGui.QCheckBox('Link',self)
        checkBox.move(offset + 820,File_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )

        checkBox = QtGui.QCheckBox('LogIn',self)
        checkBox.move(offset + 880,File_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'LogIn') )

        checkBox = QtGui.QCheckBox('Letter',self)
        checkBox.move(offset + 950,File_y)
        checkBox.stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )

        # Need Do
        project_y = 490
        checkBox1 = QtGui.QCheckBox('ToDo',self)
        #checkBox1.setStyleSheet("QCheckBox::indicator { width: 15px; height: 15px;}")
        checkBox1.move(offset + 700,project_y)
        checkBox1.stateChanged.connect(lambda state: self.tick(state, word1 = 'ToDo') )

        checkBox = QtGui.QCheckBox('NeedToCheck',self)
        checkBox.move(offset + 780,project_y)
        checkBox.stateChanged.connect(lambda state: self.tick(state, word1 = 'NeedToCheck') )
        
        


    def setAllButtonsChecked(self, state=2):
        for button in self.group.buttons():
            button.setChecked(checked)
        

    def tick(self, state, word1):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ word1 +')')   
            print(word1)         
         else:
            string.remove('(?=.*#'+ word1 +')')
            print(state) 

   

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