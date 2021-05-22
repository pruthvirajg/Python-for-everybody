"""
#**********************************************************************************************************
# Name : Assignment_7_1
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_7_1.
# Input : words.txt
# Date : 22-May-2021
#************************************************************************************************************

Question below:
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

# Answer

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
read_fh = fh.read()
read_fh = read_fh.rstrip()
print(read_fh.upper())
