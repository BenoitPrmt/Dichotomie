L = [2,6,4,8,9,1,7,5,15,14,85,13,70,10]

for i in range(len(L)-1):
    temp=L[i+1]
    while L[i]>temp and i >= 0:
        L[i+1]=L[i]
        i-=1
    L[i+1]=temp
print(L)