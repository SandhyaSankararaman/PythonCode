import math
x=int(input("Enter the x value"))
n=int(input("Enter the n value"))
sign=1
su=0.0
def facto(s):
    for i in range(1,s+1):
        fact=fact*i
    return(fact)
for i in range(1,n+2):
    p=sign*(pow(x,i)/math.factorial(i))
    sign=(-1)*sign
    su=su+p
print("sine series of",x, "upto",n,"is:",su)