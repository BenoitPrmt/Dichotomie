L = [2,6,4,8,9,1,7,5,15,14,85,13,70,10]

for i in range(len(L)):
    min=i
    for j in range(i+1,len(L)):
        if L[j]<L[min]:
            min=j
    L[i],L[min]=L[min],L[i]
print(L)