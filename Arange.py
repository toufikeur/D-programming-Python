from numpy import*
#it arrange first digit start,2nd digit end,last digit increment
r=arange(5)
roll=arange(1,8)
ro = arange(1,10,2)
rom=arange(10,1,-2)
n=len(roll)

i=0
while(i<n):
    print("Index",i ,"=",roll[i])
    i+=1
print("Or1:")

for en in roll:
    print(en)


print("or2")
print(roll)

print("2nd part:,,,,,,,,,,,,,,,,,,,,,,,,,,")
print(ro)
print("Neg Arange>>>>>>>>>>>>>>")
print(rom)

print("Only one Argument:>.>>>>.>.>>>.>.>>>>>>.>>>>")
print(r)
print("End of the code")