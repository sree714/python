#7.Write a program to calculate simple interest.Suppose the customer is a
#senior citizen., then he will get 12 percent interest and for other customers he
#will get 10 percent interest.(use function)

def simple_interest(p,t,r): 
	print('The principal is', p) 
	print('The time period is', t) 
	print('The rate of interest is',r) 
	
	si = (p * t * r)/100
	
	print('The Simple Interest is', si) 
	return si 
	

simple_interest(8, 6, 8) 
