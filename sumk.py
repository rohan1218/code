
ls=[]
n=int(input())
k=int(input())
for i in range(n):
    x=int(input())
    ls.append(x)
c=0
sum=0
for i in ls:
    sum+=i
    c+=1
    if c==k:
        break
print(sum)
