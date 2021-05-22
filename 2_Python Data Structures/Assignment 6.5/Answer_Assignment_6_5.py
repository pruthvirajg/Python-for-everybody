"""
#**********************************************************************************************************
# Name : Assignment_6_5
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_6_5.
# Input : Nothing
# Date : 22-May-2021
#************************************************************************************************************

Question below:
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
"""

# Answer

text = "X-DSPAM-Confidence:    0.8475"
found = text.find('.')
print(float(text[found-1:found+5]))