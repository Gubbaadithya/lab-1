a=int(input("enter a number"))
count=0
for i in range(1,a):
    if(a%i==0):
        count=count+i
if(count==a):
    print(a,"is perfect")
else:
    print(a,"is not perfect")
    

