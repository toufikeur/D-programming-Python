from numpy import*
# stu_id=linspace(0,6,4)
# i=0
# for i in range(0,4,1):
#     print(stu_id[i])

#First digit 1 it start, 2nd digit 8 it End , and last digit 5 it divides into 5 part
roll=linspace(1,8,5)
ro=linspace(1,8,5,endpoint=False)
n=len(roll)
m=len(ro)
i=0
while(i<n):
    print("Index",i ,"=",roll[i])
    i+=1
print("Or1:")

for en in roll:
    print(en)


print("or2")
print(roll)
print("With Endpoint")
print(ro)
print("End of the code")