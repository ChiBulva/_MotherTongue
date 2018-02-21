import os

p = open('Z.txt','r')               #Opens Local .txt file
line_1 = p.readlines()              #Reads in the .txt file as lines in a list. Ex (line 1 in txt = line_1[0])
path = line_1                       #Creates path for temperary use
print(str(line_1[0]))               #Prints Line_1 at place '0'
print(str((((len(line_1))+1)/2)))   #Prints (length of line + 1) / 2 ... (this is because we have a space between each line)
num = (((len(line_1))))				#Assigns length of line_1
num2 = (((len(line_1))+1)/2)        #

p.close()

#print(list(line_1))
#print("\n")
#print("\n")
#print("\n")
#print("Testing: \n")
#print((line_1[0]))
#print((line_1[1]))
#print((line_1[2]))
print("Length of line_1: "+str(len(line_1))+"\n")
print("\"  ")
#for x in range(len(line_1)):
#    print(str(x)+" : "+str(len(line_1[x])))

print("  \"")

line_in_file = 66 #change this number to test on each line: Ex. line_in_file = 2 it'll read line 3 of z.txt 

count = 0
pos_1 = 0
x = 0
cur = ' '
p = 0
#<-----------For loop goes here 
while(cur!=")"):
    while(p!=1): #finds start and end of word
        print("Position: "+str(x))
        cur = line_1[line_in_file][x]
        print("    Cur: "+str(cur))
        x = x+1
        count = count+1
        if cur=="(":
            pos_1 = x-2
            p = 1
    end_pos_word_start_of_descriptor = pos_1 #Munus 2 because 'x' is in the '(' position so -2 to take away the ' ('
    start_pos_word = 0 #Begining of word\
    x = x+1
    cur = line_1[line_in_file][x]
    count = count+1
    if(cur==")"):
        end_of_descriptor_start_of_definition = x+1

end_of_definition = int((len(line_1[line_in_file])-1))
print("While ran: "+str(count)+" times")
#Results of double while loop:


print("end_pos_word_start_of_descriptor: "+str(end_pos_word_start_of_descriptor))
print("end_of_descriptor_start_of_definition: "+str(end_of_descriptor_start_of_definition))
print("end_of_definition: "+str(end_of_definition))

print("\n\nWorked Great!")		
