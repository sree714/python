
#2.Write a program that validates a mobile phone number.The number should
#start with 7,8 or 9 followed by 9 digits. (use standard function)

import re 

def isValid(s): 
	Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
	return Pattern.match(s) 

s = "987654321"
if (isValid(s)): 
	print ("Valid Number")	 
else : 
	print ("Invalid Number") 

