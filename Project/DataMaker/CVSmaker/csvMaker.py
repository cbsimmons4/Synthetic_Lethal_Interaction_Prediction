f1 = open('results2.txt', 'r')
f2 = open ('idKey.txt')
csv = open('results2.csv','w')
resultsData = f1.readlines()
keyData = f2.readlines()

map = {}

for line in keyData:
	splitLine = line.split()
	key = splitLine[1]
	value = splitLine[0]
	map[key] = value

csv.write("gene,")
for i in range (2):
	csv.write("dim" + str(i+1))
	if (i != 1):
		csv.write(",")
csv.write("\n")

for line in resultsData[1:]:
	splitLine = line.split()
	csv.write(map[splitLine[0]] + ",")
	for i in range(2):
		csv.write(splitLine[i+1])
		if (i != 1):
			csv.write(",")
	csv.write("\n")


f1 = open('results24.txt', 'r')
csv = open('results24.csv','w')
resultsData = f1.readlines()

csv.write("gene,")
for i in range (24):
	csv.write("dim" + str(i+1))
	if (i != 23):
		csv.write(",")
csv.write("\n")

for line in resultsData[1:]:
	splitLine = line.split()
	csv.write(map[splitLine[0]] + ",")
	for i in range(24):
		csv.write(splitLine[i+1])
		if (i != 23):
			csv.write(",")
	csv.write("\n")

f1 = open('results128.txt', 'r')
csv = open('results128.csv','w')
resultsData = f1.readlines()

csv.write("gene,")
for i in range (128):
	csv.write("dim" + str(i+1))
	if (i != 127):
		csv.write(",")
csv.write("\n")

for line in resultsData[1:]:
	splitLine = line.split()
	csv.write(map[splitLine[0]] + ",")
	for i in range(128):
		csv.write(splitLine[i+1])
		if (i != 127):
			csv.write(",")
	csv.write("\n")



