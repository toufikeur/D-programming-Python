# x=int(input("Enter the number:"))
# for i in range(1,x,1):
#     print("Loop :",i)
#     for j in range(1,4,1):
#         print("Inner loop :",j)
# print("Rest of the code")

x=input("Enter string:")
l =len(x)
u=0
lo=0
ex=0
sp=0
for i in range(0,l,1):
    if(x[i]>='a' and x[i]<='z'):
        lo+=1
    elif(x[i]>='A' and x[i]<='Z'):
        u+=1
    elif(x[i]==' '):
        sp+=1
    else:
        ex+=1;
print("Upper case:",u,"Lower case:",lo,"Extra:",ex,"Space:",sp)
print("End of code")