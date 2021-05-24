"""
#**********************************************************************************************************
# Name : Assignment_10_2
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_10_2.
# Input : mbox-short.txt
# Date : 23-May-2021
#************************************************************************************************************

Question below:

10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

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
    for Time in Split_lines:
        if not(count_idx  == 5):  # Taking the Time index - ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
            count_idx = count_idx +1 
            continue
        else:
            count_idx = count_idx +1
            # Add the Hours to the dictionary and bring out the count for each Hour
            Hour  = Time[0:2]
            if Hour not in dixnary:
                dixnary[Hour] = 1
            else:
                dixnary[Hour] += 1 

Sorted_list = sorted((k,v) for (k,v) in dixnary.items())

for printz_k,printz_v  in Sorted_list:
    print(printz_k , printz_v)