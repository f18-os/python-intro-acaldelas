#
#################
#Alan Caldelas
#3/9/2018
#################
#
#
#Intro lab for word count
#
#! /usr/bin/env python3
#Import cmd arguments, checking if file exists, regular expressions, and executing
import sys, os, re

#set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
inputFname = sys.argv[1]
outputFname = sys.argv[2]
if not os.path.exists(inputFname):
    print(f"File {inputFname} does not exist")
    exit()


#Open file
inputread = open(inputFname, 'r')

#Dictionary
diction = {}

for line in inputread:
    line = line.strip().lower()
    for word in line.split():
        word = re.sub('[a-zA-Z]','',line)
        if word not in diction:
            diction[word] = 1
        else:
            diction += 1
inputread.close()

with open(outputFname, 'w') as file:
    for k,v in diction.items():
        w = str(k)+'\b'+str(v)+'\n'
        file.write(w)

