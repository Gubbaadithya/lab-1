#Defining the user function
def Remove(arr):
    final = []
    for num in arr:
        if num not in final:
            final.append(num)
    return final
# Main body
arr = [2,4,5,10,5,8,10]
print(arr)
newarr=Remove(arr)
print(newarr)
#for i in range (0,len(newarr)):
 # print(newarr[i])
 
