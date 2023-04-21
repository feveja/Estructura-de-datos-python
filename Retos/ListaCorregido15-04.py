import random
e=list(range(5))
print(e)
for i in range(len(e)):
    for j in range(len(e)-1):
        aux=0
        if e(j)<e(j+1) and j+1<=len(e-1):
            aux= e(j)
            e(j)=e(j+1)
            e(j+1)= aux
print(e)
