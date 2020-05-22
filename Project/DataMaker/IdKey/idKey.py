f = open('clean.txt', 'r')
idKey = open('idKey.txt','w')
allData = f.readlines()

map = {} 
next_id = 1

for i in range (len (allData)):
	line = allData[i].split()
	geneA = line[0]
	geneB = line[1]

	if (not geneA in map ):
		map[geneA] = next_id
		next_id += 1
	if (not geneB in map):
		map[geneB] = next_id
		next_id += 1

for the_key, the_value in map.items():
    idKey.write (the_key + " " + str(the_value) + " \n")
