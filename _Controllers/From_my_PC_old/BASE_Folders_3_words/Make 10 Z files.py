import os

p = open('Z.txt','r')               #Opens Local .txt file
line_1 = p.readlines()              #Reads in the .txt file as lines in a list. Ex (line 1 in txt = line_1[0])
path = line_1                       #Creates path for temperary use
print(str(line_1[0]))               #Prints Line_1 at place '0'
print(str((((len(line_1))+1)/2)))   #Prints (length of line + 1) / 2 ... (this is because we have a space between each line)
num = (((len(line_1))))				#Assigns length of line_1
num2 = (((len(line_1))+1)/2)        #

p.close()

line = []
switch = 0
count = 0
p = open('Z.txt','r')
for x in range(num+1):
    if (switch==0):
        print("switch = 0: "+str(x)+"\n")
        line.append(line_1[x])
        switch = 1
    else:
        print("switch = 1: "+str(x)+"\n")
        switch = 0


print(len(line))

for x in range(len(line)):
    if(line[x][0]!='Z'):
        print("Failed at: "+str(x))
        print(line[x])

#for x in range(num2):
#    print(str(len(line)))
#    print("\n")
