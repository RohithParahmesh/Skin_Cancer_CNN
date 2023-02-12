def printLeaders(arr, size):
    
    max_from_right = arr[size-1]  
    print (max_from_right,end=' ')   
    for i in range( size-2, -1, -1):       
        if max_from_right < arr[i]:       
            print (arr[i],end=' ')
            max_from_right = arr[i]
         
print("enter no of elements of the array")
n=int(input())
arr=[]
for i in range(0,n):
    print("enter",i,"th element of the array:")
    k=int(input())
    arr.append(k)
    
printLeaders(arr, n)