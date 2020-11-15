#1. Write a program to print the first word and last word of a string.(use
#standard function)


def FirstAndLast(string): 
	for i in range(len(string)): 
		if i == 0: 
			print(string[i], end = "") 

		if i == len(string) - 1: 
			print(string[i], end = "") 

		if string[i] == " ": 
			print(string[i - 1], 
				string[i + 1], end = "") 

if __name__ == "__main__": 
	string = "Smrity Banerjee"
	FirstAndLast(string) 

