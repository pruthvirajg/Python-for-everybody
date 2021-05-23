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


"""

# Answer

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for gline in fh:
    if gline.find('From') == -1: continue
    Split_lines = gline.split()
    if len(Split_lines)<3: continue # Removing the From: mailid@univ.edu
    print(Split_lines[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")
