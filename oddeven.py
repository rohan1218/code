a=int(input())
def check(a):
    if a<0:
        print("invalid")
    else:
        if a%2==0:
            print("even")
        else:
            print("odd")
check(a)
