from numpy import*
a=array([10,20,30,40,50])
b=a.view()

print(a)
print(b)
print("After change_______________")
a[1]=70
b[1]=90
print(a)
print(b)

print(id(a))
print(id(b))

#Id is different 
print("_____________________copy function")
c=a.copy()
a[1]=60
c[1]=80
print(a)
print(c)

print(id(a))
print(id(c))