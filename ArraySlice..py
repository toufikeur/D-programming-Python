from array import *

arr1=array('i',[1,2,3,4,5,6,7,8,9])

ln=len(arr1)

print ("Original array")

for i in range(ln):
    print (i,"=",arr1[i])
print("After slicing the array")

arC=arr1[-4:-2]
arD=arr1[0:5:1]
for i in arC:
    print (i)

print("........................")
for i in arD:
    print(i)
    
print("End of the code")