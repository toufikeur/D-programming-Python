from numpy import*
a=array([100,200,300,400])
b=array([100,20,30,500])
result= a==b
print(result)
print(any(result))
print(all(result))

result1=where(a>b,a,b)
print(result1)