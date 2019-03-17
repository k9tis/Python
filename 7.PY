
n=0
n2=(n+1)
c=6
m=[0,]
for i in range (c):
    m.append(n2) 
    n2=(n+n2)
    n=n2-n
    
print(m)


