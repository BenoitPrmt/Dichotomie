L = [2,6,4,8,9,1,7,5,15,14,85,13,70,10]

for i in range(len(L)-1):
    for j in range(len(L)-1):
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print(L)
