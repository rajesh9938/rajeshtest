a=625
r=0
while a>0:
    t=a%10
    r=r*10+t
    a=a//10
print(r)

w=[23,65,2,6,82,23]
a=len(w)
for i in range(a):
    for j in range(i+1,a):
        if w[i]>w[j] :
            w[i],w[j]=w[j],w[i]
print(w)
