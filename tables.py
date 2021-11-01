t=int(input("Enter the table you want:"))
m=int(input("enter the number upto which it should be multiplied:"))
num=1
for i in range(1,m+1):
    num=i*t
    print(i,"X",t,"=",num)  