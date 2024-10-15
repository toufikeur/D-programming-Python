from numpy import*
a=int(input("Enter array length: "))
r1=zeros(a,dtype=int)
# c1=zeros(a,dtype=int)
ar1=array([zeros(a,dtype=int),zeros(a,dtype=int)],dtype=int)
i=0
for i in range(0,2,1):
    for j in range(0,a,1):
        ar1[i][j]=int(input())
print(ar1)
for i in range(0,2,1):
    for j in range(0,a,1):
       print(i,j,"=",ar1[i][j])
print("End of the code")