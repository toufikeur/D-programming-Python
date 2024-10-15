from numpy import*
# a =array([1,2,3,4],'int')
n=int(input("enter array size:"))

a=zeros(n,dtype='int')


j=0
for j in range(0,n,1):
    a[j]=int(input("Enter value:"))
    j+=1
    

i=0
for i in range(0,n,1):
    print(a[i])
    i+=1
    
print("End of One Dymention array")

m=int(input("enter array row:"))
p=int(input("Enter the column:"))



# c=zeros(m,dtype='int')
# d=zeros(p,dtype='int')
# # b=array([[c],[d]],dtype='int')
# b=array([[zeros(m,dtype='int')],[zeros(p,dtype='int')]],dtype='int')
b=zeros((m,p),dtype='int')

x=0
y=0
for x in range(0,m,1):
    for y in range(0,p,1):
        b[x][y]=int(input("Enter value:"))
        y+=1
    x+=1
  
print(b)
for x in range(0,m,1):
    for y in range(0,p,1):
        print("index",x,y, "=",b[x][y])
        y+=1
    x+=1
    print()
print("End of Two Dymention array")
    
