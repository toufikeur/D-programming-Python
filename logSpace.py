from numpy import*
# stu_id=linspace(0,6,4)
# i=0
# for i in range(0,4,1):
#     print(stu_id[i])
##It means 10 to the power
#10^1 (10) to 10^3 (1000) and it divide it into 3 parts(last digit of 1,3,3)
roll=logspace(1,3,3)
ro=logspace(1,3,4,endpoint=False)
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