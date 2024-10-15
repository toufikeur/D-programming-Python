from numpy import*
a=ones((3,4),dtype='int')
i=0
# for i in range(0,3,1):
#     for j in range(0,4,1):
#         print(a[i][j])
#         j+=1
#     i+=1
#     print()  
while i<3:
    j=0
    while j<4:
        print(a[i][j])
        j+=1
    i+=1
    print()  
  

print("End of the code")