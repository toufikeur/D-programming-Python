from array import*

arr1=array('i',[1,2,3,4,5])
arr2=array('i',[6,7,8,9])

print ("first array")
i=0
l1=len(arr1)
l2=len(arr2)

while(i<l1):
    print(arr1[i])
    i+=1
print("second array")
i=0
while(i<l2):
    print(arr2[i])
    i+=1

arr1.extend(arr2)
l3=len(arr1)
print("Extend array")
i=0
while(i<l3):
    print(arr1[i])
    i+=1
print("End of the code")
