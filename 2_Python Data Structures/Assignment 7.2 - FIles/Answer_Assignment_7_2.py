"""
#**********************************************************************************************************
# Name : Assignment_7_2
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_7_2.
# Input : words.txt
# Date : 22-May-2021
#************************************************************************************************************

Question below:

7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the SUM() function or a variable named S*U*M in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

# Answer

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count_values = 0
Final_Target_float_value = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # The target line here
    found_colon = line.find(':')
    Target_float_value = line[found_colon+1:len(line)]
    Target_float_value = Target_float_value.rstrip()
    Target_float_value = float(Target_float_value)
    
    Final_Target_float_value = Final_Target_float_value + Target_float_value
    count_values = count_values + 1
    
    
# calculating the Average Value     
Average_value = Final_Target_float_value/count_values    
print("Average spam confidence:",Average_value)