import re

def main():
	# Init
	text = []
	sorban_end = []
	kulcs_szo_sora = []
	#key_01 = input('Adj kulcsszot : ' )
	#key_02 = input('Adj kulcsszot meg: ' )
	#key_01 = 'ToDo'
	kulcsSzo = r"(?=.*)(?=.*#" + 'BasePlus' + ")(?=.*#" + 'BaseMinus' + ")"
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
		 		 
		 	#print(hits)	 
		 	#print(lezaro)
		for megVagy in text[hits-1:lezaro-1]:			
			print(megVagy, end='' )

		print()
		print('----------------------------------oo------------------------------------')

main()
