# for i in range(int(input())):
#     s=int(input())
#     a = list(map(int, 
#     input().strip().split()))[:s]
    
#     # for j in range(s):
#     #     s =int(input())
#     #     lis.append(s)
#     # for k in range(s):
#     #     print(lis[k])
    
#     a.sort()
#     cnt =0
#     for i in range(0,s,1):
#         for k in range (i+1,s,1):
#             if(a[i]==a[k]):
#                 cnt +=1
#                 for j in range (k+1,s,1):
#                     if(a[k]!=a[j]):
#                         i=j
#                         break
                
#     print(cnt)
        
    
    
    
#     # Main code
#     # cnt =0
#     # if s==1 :
#     #     print(0)
#     # else:
#     #     cnt=0
#     #     for j in range(0,s,1):
#     #         for k in range(j+1, s, 1):
#     #             if(a[j]==a[k]) :
#     #                 cnt+=1
#     #                 break
#     #     print(cnt)

n =int(input())
for i in range(n):
    s= int(input())
    a = list(map(int, input().split()))
    print(sum([a.count(x) // 2 for x in range(s + 1)]))