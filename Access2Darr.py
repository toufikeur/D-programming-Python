from numpy import*
a=zeros((3,2),dtype=int)
n=len(a)
print(n)
print(a)
i=0
j=0
for i in range(n):
    for j in range(len(a[i])):
       a[i][j]= input("Enter values:")
    print()
print(a)
print("End of the code")