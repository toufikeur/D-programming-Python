from numpy import*

n=int(input("Enter the  array size:"))
a=zeros(n,dtype='int')
i=0

while i<n:
    a[i]=int(input("Enter value:"))
    i+=1
print()

print(a)

b=reshape(a,(2,3))
print(b)

#we can use flatten function to convert 2D and 3D arrays into 1D array
c=b.flatten()
print(c)