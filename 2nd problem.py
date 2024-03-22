x = 5  #number of books
y = 40 #price of books

if (x==2<=4):
    d = ((x*y)*0.10)
    print ("your discounted amount is : ",x*y-d)
    
elif (x==5):
    d = ((x*y)*0.20)
    print ("your discounted amount is : ",x*y-d)
    
elif (x>5):
    d = ((x*y)*0.50)
    print ("your discounted amount is : ",x*y-d)
    
else :
    print("your amount is : ",x*y)
    print ("Sorry!, you have no discount")