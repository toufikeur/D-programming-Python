from array import*
stu_id=array('i',[1,2,5,4,3])
# l=len(stu_id)
# for i in range(0,l,1):
#     print(stu_id[i])
# print("End of the code")
# print("After appending stu_id")

# stu_id.append(5)
# l=len(stu_id)
# for i in range(0,l,1):
#     print(stu_id[i])
# print("End of the code")


# from array import*

# stu=array('i',[])
# x=int(input("Enter the array size:"))
# for i in range(0,x,1):
#     stu.append(int(input("integer:")))
# for i in range(0,x,1):
#     print("All are present:",stu[i])
l=len(stu_id)
for i in range(0,l,1):
    print(stu_id[i])

print("After remove array")
stu_id.remove(2)
i=0
ln=len(stu_id)
for i in range(0,ln,1):
    print(stu_id[i])


print("After reverse array")

stu_id.reverse()
lnx=len(stu_id)
i=0
while i<lnx:
    print(stu_id[i])
    i+=1

# print("After sort")
# stu_id.sort()
# i=0
# while i<lnx:
#     print(stu_id[i])

print("End of the code")