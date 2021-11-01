#Check if the given number is a palindrome
letter=input("Enter the word:")
f=''
for i in letter:
    f=i+f
print(f)
if(f==letter):
    print("it is a palindrome")
else:
    print("It is not a palindrome")