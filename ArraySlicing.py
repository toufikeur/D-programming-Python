from numpy import*

a=array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])

print(a)
b=a[1, :]
print(b)
c=a[:,1]
print(c)
d=a[2:3, 2:3]
print(d)
e=a[0:3, 1:3]
print(e)

si=int(a.size)
print(si)
dim=int(a.ndim)
print(dim)
sh=a.shape

print(sh)

byte=a.nbytes
print(byte)
