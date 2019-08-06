n=int(input())
if n<60:
    print("0",n)
elif n>60:
    b=n//60
    c=n%60
    print(b,c)
