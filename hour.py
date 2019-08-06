n=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(len(n)):
    if m[i]>n[i]:
        a=m[i]-n[i]
        print(a,end=" ")
    else:
        b=n[i]-m[i]
        print(b,end=" ")
i+=1
