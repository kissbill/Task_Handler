import re

def main():
	# file open 
	f = open('test.txt','r')
	message = f.read()
	f.close()

	# megkeresni a --> 
	minta = re.compile("#")


	# vegig nezni a szovegben
	for i, line in enumerate(open('test.txt')):
		for match in re.finditer(minta, line):
			print ('Found on line %s ' % ( i + 1 ))
			print(line)
			#print(sor[0])

	#kiiratni a hozzatartozo linket
#	for line in sor:
#		print(line)
main()
#https://stackoverflow.com/questions/10477294/how-do-i-search-for-a-pattern-within-a-text-file-using-python-combining-regex