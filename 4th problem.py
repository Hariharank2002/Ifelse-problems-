A = int (input("1 rupee coin : "))
B = int (input("2 rupees coin : "))
C = int (input("5 rupees coin : "))
D = int (input("10 rupees coin : "))
X = int (input("totally purchased vegitables amount : "))

A=A*1
B=B*2
C=C*5
D=D*10

tot_money=A+B+C+D
if tot_money==X:
    print ("paid")
    
elif tot_money>X:
    print ("paid")
    print(tot_money-X)
    
elif tot_money<X:
    print ("Notpaid")
    print(tot_money)
    
else:
    print ("kadan anbai murikum")