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
import sys, os, re, subprocess

#set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
textFname = sys.argv[1]
outputFname = sys.argv[2]



