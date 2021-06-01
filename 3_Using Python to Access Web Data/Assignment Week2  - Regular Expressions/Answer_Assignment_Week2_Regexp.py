"""
#**********************************************************************************************************
# Name : Answer_Assignment_Week2_Regexp
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Answer_Assignment_Week2_Regexp.
# Input : regex_sum_42.txt / regex_sum_1193723.txt
# Date : 23-May-2021
#************************************************************************************************************

"""

# Answer
import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1193723.txt"
    
handle = open(name)

dList = list()
for gline in handle:
    x_found = re.findall("[0-9]+", gline)
    test_list = [int(i) for i in x_found]
    if test_list:
        dList.extend(test_list)
    # x_found_int = list(map(int, x_found))
#     dList.extend(x_found)
    
print(sum(dList))

