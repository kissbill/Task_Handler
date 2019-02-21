import re

def main():
	# Init
	tomb = []
	text = []
	sorban_end = []
	sorban_keyword = []
	keresztLezaro = 0
	
	

	# Set what Searching
	#keyword = 'Automat'
	ending = '\\+'

	#pattern_keyword = re.compile( "#" + keyword )
	pattern_keyword = re.compile( "#ToDo" )
	pattern_end = re.compile( ending )

	# Loop through text
	for i, line in enumerate(open('test.txt')):
		#line = line.strip()
		#print( i + 1 , line, end='' )
		text.append(line)
		#Kulcs szo
		for match in re.finditer(pattern_keyword, line):
			#print ('Found on line %s: %s' % (i+1, match.groups()))
			tomb.append(line) #a keresett sor
			#print( i + 1 ) #hanyas sorba
			sorban_keyword.append( i + 1 ) #talalt sor lementese
		# Kereszt lezarasok keresese
			for match in re.finditer(pattern_end, line):
				sorban_end.append( i + 1 ) #talalt kereszt sor lementese
				if kereszt > sorban_keyword[]:
					keresztLezaro = kereszt
		 
	


	# Lezaro elem legyen nagyobb mint a keresett kulcs szo
	#for kereszt in sorban_end:
	##	if kereszt > sorban_keyword[]:
		#	keresztLezaro = kereszt
		#	break


	# Print findings
	for hits in tomb:
		print()
		print(sorban_keyword)
		print('Talalat a sorban : ' + hits) #a megtalalt sor
		#print('Osszes sor : %s ' % (i)) #osszes sor

	for ends in sorban_end:
		print( ' Sor lezarasok %s' % ( ends ))

	print()

	#for megVagy in text[sorban_keyword-1:keresztLezaro]:
		#print(megVagy, end='' )



main()
