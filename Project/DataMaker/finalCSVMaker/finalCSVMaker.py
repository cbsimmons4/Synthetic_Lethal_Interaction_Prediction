import copy
f1 = open('roguev-sp-emap-gis-std.tsv', 'r')
f2 = open('results24.csv', 'r')
bigFile = open('final.csv','w')
interationData = f1.readlines()
pointData = f2. readlines()

num_dim = 24
map = {}


for line in pointData[1:]:
	#print (line)
	cur_line = line.split(',')
	cur_line_string = copy.deepcopy(line)
	map[ cur_line[0] ] = cur_line_string.strip()

#print (map)
bigFile.write("geneA,")
for i in range (num_dim):
	bigFile.write("Adim" + str(i + 1) + ",")
bigFile.write("geneB,")
for i in range (num_dim):
	bigFile.write("Bdim" + str(i + 1) + ",")
bigFile.write("score,")
bigFile.write("catagory,\n")


for line in interationData[1:]:
	cur_line = line.split()
	#print (cur_line)
	bigFile.write(map[cur_line[0]] + "," + map[cur_line[1]] + "," +  cur_line[2] + "," + cur_line[3] + "\n")
