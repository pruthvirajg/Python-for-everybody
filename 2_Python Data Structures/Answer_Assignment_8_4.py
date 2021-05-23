"""
#**********************************************************************************************************
# Name : Assignment_8_4
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_8_4.
# Input : words.txt
# Date : 22-May-2021
#************************************************************************************************************

Question below:

8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

# Answer

fname = input("Enter file name: ")
fh = open(fname)
lst = list()


for line in fh:
    Split_lines = line.split()
    for var in Split_lines:
        if not(var in lst):
            lst.append(var)

lst.sort()
print(lst)
