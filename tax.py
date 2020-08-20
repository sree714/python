tax = 0
n1 = int(input('Enter income: '))
if(n1 >= 500000 and n1 <1000000):
    tax = (10 / 100) * n1
    print("Tax: ",tax)

if(n1 >= 1000000 and n1 < 1500000):
    tax = (20 / 100) * n1
    print("Tax: ",tax)

if(n1 >= 1500000):
    tax = (30 / 100) * n1
    print("Tax: ",tax)
else:
    print("no tax")