a=int(input("a:"))

if a in range(2,6):
    a+=10
elif a in range(7,40):
    a-=100
elif a>0:
    a*=3
elif a<3000:
    a*=3
else: 
    a=0
print(a)
