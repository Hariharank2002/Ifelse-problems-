N = 1
remainder = N
if (remainder>=5 and remainder/5):
    remainder = int(remainder%5)
    print("count of rupees 5 : ",int(remainder/5))
if (remainder >= 2 and remainder/2):
    print ("count of rupees 2 : ",int(remainder/2))
    remainder = int(remainder%2)
if(remainder > 0):
    print ("count of rupee  1 : ",remainder)    
    
    
    
