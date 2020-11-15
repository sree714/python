#5.Write a program that replaces , and ; from a string with a blank space.

string = "Once in,a;bluemoon";  
ch = ' ';  
   
string = string.replace(',', ch);  
string = string.replace(';', ch);  
   
print("String after replacing , with given character: ");  
print(string);  