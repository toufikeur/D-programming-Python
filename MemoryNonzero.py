from numpy import*
a=array([100,1,2,0,3,0,4])
result = nonzero(a)
print(result)


print("----------------------------------")

b=a
print(a)
print(b)
print(id(a))
print(id(b))
print("End of the code")

#it provides same memory location but it adds different tag.
#so in one memory location we can add more variable but its tag is different
#it saves memory space.It's unique from C or c++ language
