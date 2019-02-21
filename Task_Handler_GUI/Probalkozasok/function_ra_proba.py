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
        self.setStyleSheet('font-size: 14pt; font-family: Europa;')

        opening = QtGui.QPushButton( 'Open' )
        searching = QtGui.QPushButton( 'Search' )
        exit = QtGui.QPushButton( 'EXIT' )        
        #Projects ################################################
        project_names = ['BasePlus','BaseMinus','Spa','Ltc','P514','Software','SWChange']        
        pN={}
        #Topics ################################################
        topics_names = ['Offset','ModeManager','ActiveDischarge','ODIS','Automat']
        tN={}
        # Works ################################################
        work_names = ['Requirment','Defect','Meeting','Regession','Review','Nightly']
        wN={}
        # Miscs ################################################
        misc_names = ['AddWorkFlow','KnowHow','Directiva']
        mN={}
        # Infrastructs #####################################################
        infrastruct_names = ['Git','Polarion','Jenkins','MiniHIL','Gerrit']
        iN={}
        # Tools #####################################################
        tool_names = ['CANape','CANoe','ECUtest','Trace']
        toN={}
        file_names = ['File','Xlsx','Link','LogIn','Letter']
        fN={}
        needDo_names = ['ToDo','NeedToCheck']
        nN={}        

        def tick_box_creation(arrays,shortName):
            for x in range(0,len(arrays)):
                shortName["checkBox_{0}".format(x)]=QtGui.QCheckBox(arrays[x],self)

        def placing_tick_box(arrays,shortName,lines):
                for x in range( 0 , len( arrays) ):
                    grid_layout.addWidget( shortName['checkBox_' + str(x)], lines , x ) 

        tick_box_creation(project_names,pN)
        tick_box_creation(topics_names,tN)
        tick_box_creation(work_names,wN)
        tick_box_creation(misc_names,mN)
        tick_box_creation(infrastruct_names,iN)
        tick_box_creation(tool_names,toN)
        tick_box_creation(file_names,fN)
        tick_box_creation(needDo_names,nN)

        placing_tick_box(project_names,pN,0)
        placing_tick_box(topics_names,tN,1)
        placing_tick_box(work_names,wN,2)
        placing_tick_box(misc_names,mN,3)
        placing_tick_box(infrastruct_names,iN,4)
        placing_tick_box(tool_names,toN,5)
        placing_tick_box(file_names,fN,6)
        placing_tick_box(needDo_names,nN,7)

        # Gombok #####################################################
        gombok_line = 8        
        grid_layout.addWidget( searching, gombok_line , 8 )
        grid_layout.addWidget( opening, gombok_line , 0)
        grid_layout.addWidget( exit, gombok_line , 1)
        #####################################################          
        
        miez =tN['checkBox_0'].isChecked()
        print(miez)

        #for x in range( 0 , len(project_names) ):
        #	pN['checkBox_' + str(x)].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[x]) )
        pN['checkBox_0'].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[0]) )
        pN['checkBox_1'].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[1]) ) 
        pN['checkBox_2'].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[2]) )        
        pN['checkBox_3'].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[3]) ) 
        pN['checkBox_4'].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[4]) ) 
        # Topics
        tN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = topics_names[0]) )
        tN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = topics_names[1]) )
        tN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = topics_names[2]) )
        tN['checkBox_3'].stateChanged.connect( lambda state: self.tick(state, word1 = topics_names[3]) )
        tN['checkBox_4'].stateChanged.connect( lambda state: self.tick(state, word1 = topics_names[4]) )
        # Works        
        wN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Requirment') )
        wN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Defect') ) 
        wN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Meeting') )
        wN['checkBox_3'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Regession') )
        wN['checkBox_4'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Review') )
        wN['checkBox_5'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Nightly') )
        #    Miscs
        mN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = 'AddWorkFlow') )
        mN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = 'KnowHow') )
        mN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Directiva') )
        #checkBox_17.stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )
        #checkBox_18.stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )
        # Infrastructs
        iN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Git') )
        iN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Polarion') )
        iN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Jenkins') )
        iN['checkBox_3'].stateChanged.connect( lambda state: self.tick(state, word1 = 'MiniHIL') )
        iN['checkBox_4'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Gerrit') )
        # Tools
        iN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = 'CANape') )
        iN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = 'CANoe') )
        iN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = 'ECUtest') )
        iN['checkBox_3'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Trace') )
        # File_releated
        fN['checkBox_0'].stateChanged.connect( lambda state: self.tick(state, word1 = 'File') )
        fN['checkBox_1'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Xlsx') )
        fN['checkBox_2'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Link') )
        fN['checkBox_3'].stateChanged.connect( lambda state: self.tick(state, word1 = 'LogIn') )
        fN['checkBox_4'].stateChanged.connect( lambda state: self.tick(state, word1 = 'Letter') )
        # Need Do
        nN['checkBox_0'].stateChanged.connect(lambda state: self.tick(state, word1 = 'ToDo') )
        nN['checkBox_1'].stateChanged.connect(lambda state: self.tick(state, word1 = 'NeedToCheck') )       
        
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