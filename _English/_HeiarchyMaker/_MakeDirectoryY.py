#####################################################
#
#  Function: 	This will parse a single letter 
#		  of the alphabet into a 3 text files
#
######################################################

import os

path = "./_Parsed/_Y"
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise
# Read text file from the folder above
#Assign lines 8870-EOF
count=0

with open(path+"/word_Y.txt", "r") as ins:
    alpha = []
    #for alph in ins:
    for alph in ins:
    	count=count+1;
	#Assigns each line of txt file with no newline
        alpha.append(alph.rstrip('\n'))
	#print(alpha[alph])

#Grab Des
with open(path+"/descriptor_Y.txt", "r") as ins:
    descriptor = []
    #for alph in ins:
    for alph in ins:
    	count=count+1;
	#Assigns each line of txt file with no newline
        descriptor.append(alph.rstrip('\n'))
	#print(alpha[alph])

#Grab Def
with open(path+"/definition_Y.txt", "r") as ins:
    definition = []
    #for alph in ins:
    for alph in ins:
    	count=count+1;
	#Assigns each line of txt file with no newline
        definition.append(alph.rstrip('\n'))

print(count)

#Close file
ins.close()

#
newpath = "./_Files"
try:
	os.makedirs(newpath)
except OSError:
	if not os.path.isdir(newpath):
		raise
definitionWord="/definition.txt"
descriptorWord="/descriptor.txt"


for line in range(0,len(alpha)):
	#print("Running for: "+str(alpha[line])+"	"+str(line))
#	print("Running for: "+str(line))
	word="/"+str(alpha[line])
	
	newpath = "./_Files"
#	print(word)
#	print(definition[line])
#	print(descriptor[line])
	for i in range(len(alpha[line])):
		newpath=newpath+"/"+alpha[line][i]
#		print(newpath)	
		try:
			os.makedirs(newpath)
		except OSError:
			if not os.path.isdir(newpath):
				raise
		if(i==len(alpha[line])-1):
			newfile=open(newpath+word,'w')
			newfile.write(word)
			newfile.close()
			newfile=open(newpath+definitionWord,'w')
			newfile.write(definition[line])
			newfile.close()
			newfile=open(newpath+descriptorWord,'w')
			newfile.write(descriptor[line])
			newfile.close()

#print(alpha)
'''
for position in range(26):
	path = "./_Parsed"
	with open("../_AllWords/"+str(alpha[position]), "r") as ins:
	    array = []
	    for line in ins:
		#Assigns each line of txt file with no newline
	        array.append(line.rstrip('\n'))

	#Close file
	ins.close()
	
	#Sets cound to the length of the array
	count=len(array)
	#print(array[400]+"Test")
	
	#Take away "#" to comment out code
	
	#print("Count: "+str(count)+"\n")
	count2=0
	
	path = str(path)+"/_"+str(array[0][0])
	try: 
	    os.makedirs(path)
	except OSError:
	    if not os.path.isdir(path):
	        raise


	wordfile=open("_Parsed/_"+str(array[0][0])+"/word_"+str(array[0][0])+".txt","w")
	#print("_Parsed/_"+str(array[0][0])+"/word_"+str(array[0][0])+".txt")
	descriptorfile=open("_Parsed/_"+str(array[0][0])+"/descriptor_"+str(array[0][0])+".txt","w")
	#print("_Parsed/_"+str(array[0][0])+"/descriptor_"+str(array[0][0])+".txt")
	definitionfile=open("_Parsed/_"+str(array[0][0])+"/definition_"+str(array[0][0])+".txt","w")
	#print("_Parsed/_"+str(array[0][0])+"/definition_"+str(array[0][0])+".txt")


	for line in range(0,count,2):
		#print("Running for: "+str(line))
		#Searches through the individule word and will find the "(", and the ")"
		for i in range(len(array[line])):
			#does it have a "("
			if(array[line][i]=="("):
				open_par=i
			#does it have a ")"
			if(array[line][i]==")"):
				closed_par=i
				break

		word = [open_par]
		descriptor = [closed_par-open_par]
		definition = [len(array[line])-closed_par]
	
		word = array[line][0:open_par-1]
		descriptor = array[line][open_par:closed_par+1]
		definition = array[line][closed_par+2:len(array[line])]

		wordfile.write(word+"\n")
		descriptorfile.write(descriptor+"\n")
		definitionfile.write(definition+"\n")


	wordfile.close()
	descriptorfile.close()
	definitionfile.close()

print("Parsed;)")
'''
