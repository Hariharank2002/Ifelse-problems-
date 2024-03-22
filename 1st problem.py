x,y,z = 100,200,300

if ( x==y ):
    d = ( (x + y) *0.10 )
    print ("your discounted amount is : ", x+y+z-d)     
elif ( y==z ):
    d = ( (y+z) *0.10 )
    print ("your discounted amount is : ", x+y+z-d)     
    
elif ( z==x ):
    d = ( (z+x) *0.10)
    print ("your discounted amount is : ", x+y+z-d)     
else :
    print ("your amount is : ", x+y+z)
    print ("Sorry!, you have no discount")