import re
import string

# function to intake groceryItem file and loop through it converting it into a total frequency for each item
def totalFrequency():
	items ={}
	file = open("groceryItem.txt", 'a')
	file.write("\n")
	file.close()
	file = open("groceryItem.txt", 'r')
	 # loop to identify and assign frequency of unique items
	for each in file:
		if each != "\n":
			if each not in items:
				items[each] = 1

			elif each in items:
				items[each] += 1 
	# organize our grocery list output and display			
	for k in sorted(items):
		print(k.strip(), items[k])

	return 1
 # function for displaying a single and specific item
def itemFrequency(var):
	items = {}
	file = open("groceryItem.txt", 'a')
	file.write("\n")
	file.close()
	file = open("groceryItem.txt", "r")
	  # loop to identify and assign frequency of unique items
	for each in file:
		if each != "\n":
			if each.strip() not in items:
				items[each.strip()] = 1

			elif each.strip() in items:
				items[each.strip()] += 1 
	# logic for determing if user entered a valid item
	if var in items:
		print(f'{var}: {items[var]}')
	else:
		print("Item not found.")

	return 1


# function for taking our organized grocery list and putting it into a DAT file
def dataFile():
	items ={}
	outfile = open("groceryItem.txt", 'a')
	outfile.write("\n")
	outfile.close()
	infile = open("groceryItem.txt", 'r')
	
	# loop to identify and assign frequency of unique items
	for each in infile:
		if each != "\n":
			if each not in items:
				items[each] = 1

			elif each in items:
				items[each] += 1
	
	infile.close()
	freq = open('frequency.dat', 'w+')
	# writing to DAT file 
	for k in sorted(items):
		freq.write(f'{k.strip()} {items[k]}\n')

	freq.close()

	return 1
# function to read from DAT file and form histogram
def readFile():
	datFile = open('frequency.dat', 'r')
	# loop to read through DAT file and split lines into words
	for line in datFile:
		for word in line.split():
			if word.isnumeric():
				print(int(word) * "*")
			else:
				print(word)

	datFile.close()
