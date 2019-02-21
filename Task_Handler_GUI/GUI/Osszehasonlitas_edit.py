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
        #super(Window, self).__init__()
        #self.initUI()

        QtGui.QWidget.__init__(self)

        self.titleEdit = QtGui.QTextEdit()
        self.titleEdit.setFontPointSize(12)
        grid_layout = QtGui.QGridLayout()
        self.setStyleSheet('font-size: 9.7pt; font-family: Europa;')

        opening = QtGui.QPushButton( 'Open' )
        searching = QtGui.QPushButton( 'Search' )
        exit = QtGui.QPushButton( 'EXIT' )
        # Projects
        checkBox_0 = QtGui.QCheckBox('Base +',self)
        checkBox_1 = QtGui.QCheckBox('Base -',self)
        checkBox_2 = QtGui.QCheckBox('Software',self)
        checkBox_3 = QtGui.QCheckBox('SWChange',self)
        # Topics
        checkBox_4 = QtGui.QCheckBox('Offset',self)
        checkBox_5 = QtGui.QCheckBox('ModeManager',self)
        checkBox_6 = QtGui.QCheckBox('ActiveDischarge',self)
        checkBox_7 = QtGui.QCheckBox('Automat',self)
        # Works
        checkBox_8  = QtGui.QCheckBox('Requirment',self)
        checkBox_9  = QtGui.QCheckBox('Defect',self)
        checkBox_10 = QtGui.QCheckBox('Meeting',self)
        checkBox_11 = QtGui.QCheckBox('Regession',self)
        checkBox_12 = QtGui.QCheckBox('Review',self)
        checkBox_13 = QtGui.QCheckBox('Nightly',self)
        #    Miscs
        checkBox_14 = QtGui.QCheckBox('AddWorkFlow',self)
        checkBox_15 = QtGui.QCheckBox('KnowHow',self)
        checkBox_16 = QtGui.QCheckBox('Directiva',self)         
        checkBox_17 = QtGui.QCheckBox('Letter',self)
        checkBox_18 = QtGui.QCheckBox('Link',self)
        # Infrastructs
        checkBox_19 = QtGui.QCheckBox('Git',self)
        checkBox_20 = QtGui.QCheckBox('Polarion',self)
        checkBox_21 = QtGui.QCheckBox('Jenkins',self)
        checkBox_22 = QtGui.QCheckBox('MiniHIL',self)
        # Tools
        checkBox_23 = QtGui.QCheckBox('CANape',self)
        checkBox_24 = QtGui.QCheckBox('CANoe',self)
        checkBox_25 = QtGui.QCheckBox('ECUtest',self)
        checkBox_26 = QtGui.QCheckBox('ECUtest',self)
        # File_releated
        checkBox_27 = QtGui.QCheckBox('File',self)
        checkBox_28 = QtGui.QCheckBox('Xlsx',self)
        checkBox_29 = QtGui.QCheckBox('Link',self)
        checkBox_30 = QtGui.QCheckBox('LogIn',self)
        checkBox_31 = QtGui.QCheckBox('Letter',self)
        # Need Do
        checkBox_32 = QtGui.QCheckBox('ToDo',self)
        checkBox_33 = QtGui.QCheckBox('NeedToCheck',self)
       # checkBox_ = QtGui.QCheckBox('',self)
        
        #horizontalLayout = QtGui.QHBoxLayout()
     
        # Gombok
        gombok_line = 8
        
        grid_layout.addWidget( searching, gombok_line , 0 )
        grid_layout.addWidget( opening, gombok_line , 5)
        grid_layout.addWidget( exit, gombok_line , 8)

        # Projects
        project_line = 0
        grid_layout.addWidget( checkBox_0, project_line , 0 )
        grid_layout.addWidget( checkBox_1, project_line , 1 )
        grid_layout.addWidget( checkBox_2, project_line , 2 )
        grid_layout.addWidget( checkBox_3, project_line , 3 )
        # Topics
        topics_line = 1
        grid_layout.addWidget( checkBox_4, topics_line , 0 )
        grid_layout.addWidget( checkBox_5, topics_line , 1 )
        grid_layout.addWidget( checkBox_6, topics_line , 2 )
        grid_layout.addWidget( checkBox_7, topics_line , 3 )
        # Works
        work_line = 2 
        grid_layout.addWidget( checkBox_8 , work_line , 0 )
        grid_layout.addWidget( checkBox_9 , work_line , 1 )
        grid_layout.addWidget( checkBox_10, work_line , 2 )
        grid_layout.addWidget( checkBox_11, work_line , 3 )
        grid_layout.addWidget( checkBox_12, work_line , 4 )
        grid_layout.addWidget( checkBox_13, work_line , 5 )
        #    Miscs
        misc_line = 3
        grid_layout.addWidget( checkBox_14, misc_line , 0 )
        grid_layout.addWidget( checkBox_15, misc_line , 1 )
        grid_layout.addWidget( checkBox_16, misc_line , 2 )
        grid_layout.addWidget( checkBox_17 , misc_line , 3 )
        grid_layout.addWidget( checkBox_18 , misc_line , 4 )
        # Infrastructs
        infrastuct_line = 4
        grid_layout.addWidget( checkBox_19 , infrastuct_line , 0)
        grid_layout.addWidget( checkBox_20 , infrastuct_line , 1)
        grid_layout.addWidget( checkBox_21 , infrastuct_line , 2)
        grid_layout.addWidget( checkBox_22 , infrastuct_line , 3)        
        # Tools
        tool_line = 5
        grid_layout.addWidget( checkBox_23 , tool_line , 0)
        grid_layout.addWidget( checkBox_24 , tool_line , 1)
        grid_layout.addWidget( checkBox_25 , tool_line , 2)
        grid_layout.addWidget( checkBox_26 , tool_line , 3)

        # File_releated
        file_line = 6
        grid_layout.addWidget( checkBox_27 , file_line , 0)
        grid_layout.addWidget( checkBox_28 , file_line , 1)
        grid_layout.addWidget( checkBox_29 , file_line , 2)
        grid_layout.addWidget( checkBox_30 , file_line , 3)
        grid_layout.addWidget( checkBox_31 , file_line , 4)
        # Need Do
        need_line = 7
        grid_layout.addWidget( checkBox_32 , need_line , 0)
        grid_layout.addWidget( checkBox_33 , need_line , 1)
        # Projects
        checkBox_0.stateChanged.connect(lambda state: self.tick(state, word1 = 'BasePlus') )
        checkBox_1.stateChanged.connect(lambda state: self.tick(state, word1 = 'BaseMinus') )        
        checkBox_2.stateChanged.connect(lambda state: self.tick(state, word1 = 'Software') )
        checkBox_3.stateChanged.connect(lambda state: self.tick(state, word1 = 'SWChange') )
        # Topics
        checkBox_4.stateChanged.connect( lambda state: self.tick(state, word1 = 'Offset') )
        checkBox_5.stateChanged.connect( lambda state: self.tick(state, word1 = 'ModeManager') )
        checkBox_6.stateChanged.connect( lambda state: self.tick(state, word1 = 'ActiveDischarge') )
        # Works
        checkBox_7.stateChanged.connect( lambda state: self.tick(state, word1 = 'Automat') )
        checkBox_8.stateChanged.connect( lambda state: self.tick(state, word1 = 'Requirment') )
        checkBox_9.stateChanged.connect( lambda state: self.tick(state, word1 = 'Defect') ) 
        checkBox_10.stateChanged.connect( lambda state: self.tick(state, word1 = 'Meeting') )
        checkBox_11.stateChanged.connect( lambda state: self.tick(state, word1 = 'Regession') )
        checkBox_12.stateChanged.connect( lambda state: self.tick(state, word1 = 'Review') )
        checkBox_13.stateChanged.connect( lambda state: self.tick(state, word1 = 'Nightly') )
        #    Miscs
        checkBox_14.stateChanged.connect( lambda state: self.tick(state, word1 = 'AddWorkFlow') )
        checkBox_15.stateChanged.connect( lambda state: self.tick(state, word1 = 'KnowHow') )
        checkBox_16.stateChanged.connect( lambda state: self.tick(state, word1 = 'Directiva') )
        checkBox_17.stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )
        checkBox_18.stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )
        # Infrastructs
        checkBox_19.stateChanged.connect( lambda state: self.tick(state, word1 = 'Git') )
        checkBox_20.stateChanged.connect( lambda state: self.tick(state, word1 = 'Polarion') )
        checkBox_21.stateChanged.connect( lambda state: self.tick(state, word1 = 'Jenkins') )
        checkBox_22.stateChanged.connect( lambda state: self.tick(state, word1 = 'MiniHIL') )
        # Tools
        checkBox_23.stateChanged.connect( lambda state: self.tick(state, word1 = 'CANape') )
        checkBox_24.stateChanged.connect( lambda state: self.tick(state, word1 = 'CANoe') )
        checkBox_25.stateChanged.connect( lambda state: self.tick(state, word1 = 'ECUtest') )
        checkBox_26.stateChanged.connect( lambda state: self.tick(state, word1 = 'Trace') )
        # File_releated
        checkBox_27.stateChanged.connect( lambda state: self.tick(state, word1 = 'File') )
        checkBox_28.stateChanged.connect( lambda state: self.tick(state, word1 = 'Xlsx') )
        checkBox_29.stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )
        checkBox_30.stateChanged.connect( lambda state: self.tick(state, word1 = 'LogIn') )
        checkBox_31.stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )
        # Need Do
        checkBox_32.stateChanged.connect(lambda state: self.tick(state, word1 = 'ToDo') )
        checkBox_33.stateChanged.connect(lambda state: self.tick(state, word1 = 'NeedToCheck') )       

        # Gombok
        exit.clicked.connect(self.close_application)
        opening.clicked.connect(self.file_open)
        searching.clicked.connect(self.searching)
        

        verticalLayout = QtGui.QVBoxLayout( self )

        verticalLayout.addLayout( grid_layout )

        verticalLayout.addWidget( self.titleEdit )

        self.setLayout( verticalLayout )
        
        verticalLayout.addLayout( grid_layout )

        self.setGeometry( 300, 300, 900, 900 )
        self.setWindowTitle( 'DataBase for HashTagging' )
        self.titleEdit.setReadOnly(True)
   
        


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
        self.titleEdit.append(" ")
        finding_ = "".join(str(x) for x in finding)

        self.titleEdit.append(finding_)
        self.init()
        

        #finding_ = "".join(str(x) for x in urit)

    def empty_array(self):
        self.titleEdit.clear()

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