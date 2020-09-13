def search(a,m):
    for i in range(0,len(a)):
        if(a[i]==m):
            print(m,"is found in",i,"th index")
            break
k=int(input("size of array:"))
list=[]
for i in range(0,k):
    ap=int(input("array elements:"))
    list.append(ap)
m=int(input("element to search:"))   
search(a,m)
