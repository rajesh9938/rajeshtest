a=625
r=0
while a>0:
    t=a%10
    r=r*10+t
    a=a//10
print(r)