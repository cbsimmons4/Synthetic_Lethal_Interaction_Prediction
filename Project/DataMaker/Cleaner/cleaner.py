f1 = open('clean.txt', 'r')
f2 = open ('idKey.txt')
cleanerFixed = open('cleanerFixed.txt','w')
cleanData = f1.readlines()
keyData = f2.readlines()

map = {}

for line in keyData:
	splitLine = line.split()
	key = splitLine[0]
	value = splitLine[1]
	map[key] = value

for line in cleanData:
	splitLine = line.split()
	geneA = splitLine[0]
	geneB = splitLine[1]
	cleanerFixed.write(map[geneA] + " " + map[geneB] + "\n" )