def main():
	# read File
	file = open('test.txt','r')
	lines = file.readlines()
	file.close()

	# look for patterns
	for line in lines:
		line = line.strip() #levesz minden space-t stb
		print(line)
		if line == "-->":
			print(line)
	#display results

main()