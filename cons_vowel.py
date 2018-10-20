ls=['a','e','i','o','u']
a=input()
def cons_vow(a):
    if a>='A' and a<='Z' or a>='a' and a<='z':
        if a in ls:
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("invalid")
cons_vow(a)
    
