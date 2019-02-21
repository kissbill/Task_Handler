import re

def main():
	# Init
	talalat = []
	text = []
	nyit_zar = []
	sorban_end = []
	kulcs_szo_sora = []
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
			talalat.append(line) #a keresett sor
			#print( i + 1 ) #hanyas sorba
			kulcs_szo_sora.append( i + 1 ) #talalt sor lementese
		# Kereszt lezarasok keresese
		for match in re.finditer(pattern_end, line):
			sorban_end.append( i + 1 ) #talalt kereszt sor lementese
		 
	# Lezaro elem legyen nagyobb mint a keresett kulcs szo
	
	#print('megtalalt #szavak : ')
	#print(kulcs_szo_sora)
	#print()
	#print(sorban_end)
	#print('---------------------------')
	#print('Osszes sor : %s ' % (i))
	#print('---------------------------')
	hossz = len(kulcs_szo_sora)

	# Print findings
	for hits in kulcs_szo_sora:		
		#print('Talalat a sorban : ' + hits) #a megtalalt sor
		 #osszes sor
		for lezaro in sorban_end[0:hossz]:
		 	if hits < lezaro:
		 		 #print(hits)
		 		 #print(lezaro)
		 		 break
		for megVagy in text[hits-1:lezaro-1]:
			
			print(megVagy, end='' )
		print()
		print('----------------------------------------------------------------------')




	



main()
