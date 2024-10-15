from numpy import*

a=array([[1,2,3,4],[5,6,7,8],[11,12,13,14]])

# for r in a:
#     for x in r:
#         print(x)
#     print()

n=len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()
i=0
while (i<n):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    print()
    i+=1
print("End of the code")
