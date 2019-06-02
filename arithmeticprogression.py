a,b,c=input().split()
n=0
for i in range(0,int(a)):
  n+=int(b)
  b=int(b)+int(c)
print(n)
