#####################################################
#
#  Function: 	This will parse a single letter 
#		  of the alphabet into a 3 text files
#
######################################################
import os

path = "./_Parsed"
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise
# Read text file from the folder above
#Assign lines 8870-EOF
count=0

with open("alpha", "r") as ins:
    alpha = []
    for alph in ins:
	#Assigns each line of txt file with no newline
        alpha.append(alph.rstrip('\n'))

#Close file
ins.close()

#print(alpha)

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
	
	path = str(path)+"/_"+str(alpha[position])
	try: 
	    os.makedirs(path)
	except OSError:
	    if not os.path.isdir(path):
	        raise

	print("Checking for: "+str(alpha[position])+"\n")
	wordfile=open("_Parsed/_"+str(alpha[position])+"/word_"+str(alpha[position])+".txt",'w')
	#print("_Parsed/_"+str(alpha[position])+"/word_"+str(alpha[position])+".txt")
	descriptorfile=open("_Parsed/_"+str(alpha[position])+"/descriptor_"+str(alpha[position])+".txt",'w')
	#print("_Parsed/_"+str(alpha[position])+"/descriptor_"+str(alpha[position])+".txt")
	definitionfile=open("_Parsed/_"+str(alpha[position])+"/definition_"+str(alpha[position])+".txt",'w')
	#print("_Parsed/_"+str(alpha[position])+"/definition_"+str(alpha[position])+".txt")


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


#os.remove("_Parsed/__~01A~/*txt")
#os.remove("_Parsed/__~01A~")

#os.remove("_Parsed/__~01A~/*txt")
sh.rm(sh.glob('_Parsed/__~01A~/*.txt'))

print("Parsed;)")
