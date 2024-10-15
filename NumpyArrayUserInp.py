from numpy import*
n=int(input("Enter the array size:"))
arr1=zeros(n,dtype=int)
i=0
# for i in range(0,n,1):
while i<n:
    arr1[i]=input()
    i+=1

print(arr1)
print(type(arr1))
print("End of the code")