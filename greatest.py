a=int(input())
b=int(input())
c=int(input())
def greatest(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
greatest(a,b,c)
