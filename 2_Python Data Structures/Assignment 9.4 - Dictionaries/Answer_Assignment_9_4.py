"""
#**********************************************************************************************************
# Name : Assignment_9_4
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_9_4.
# Input : mbox-short.txt
# Date : 23-May-2021
#************************************************************************************************************

Question below:

9.4 Write a program to read through the mbox-short.txt and 
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as 
the person who sent the mail. 
The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.

"""

# Answer

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

dixnary = dict()
for gline in handle:
    if gline.find('From') == -1: continue
    Split_lines = gline.split()
    if len(Split_lines)<3: continue # Removing the From: mailid@univ.edu
    count_idx = 0
    for person in Split_lines:
        if not(count_idx  == 1): 
            count_idx = count_idx +1 
            continue
        else:
            count_idx = count_idx +1
            if person not in dixnary:
                dixnary[person] = 1
            else:
                dixnary[person] += 1   

all_values = dixnary.values()
max_value = max(all_values)

max_key = max(dixnary, key=dixnary.get)



print(max_key, max_value)
