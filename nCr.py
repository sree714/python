import math
nval = int(input("Enter value of n: "));  
rval = int(input("Enter value of r: "));  

n = nval
r = rval
npr = math.factorial(n)/math.factorial(n-r);  
print("nPr =",npr);


#6.Writa a program to compute P(n,r) and C(n,r) using function.
def nCr(n, r): 

	return (fact(n) / (fact(r) 
				* fact(n - r))) 

def fact(n): 

	res = 1
	
	for i in range(2, n+1): 
		res = res * i 
		
	return res 


print("nCr = ",int(nCr(n, r))) 
