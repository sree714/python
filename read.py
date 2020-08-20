a=9
b=0
nv = 0
pv = 0
z = 0
while(a >= b):
   
    n1 = int(input('Enter a number: '))
    
    if n1 < 0:
        nv = nv + 1
        print("-")
    if n1 > 0:
        pv = pv + 1
        print("+")
    if n1 == 0:
        z = z + 1
        print("0")
    if n1 == -1:
        print("- : " ,nv)
        print("+ : " ,pv)
        print("0 : " ,z)
        exit(-1)

