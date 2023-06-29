#Write a Python script to enter an y number and check its prime or not

n=int(input("Enter a number:"))
a=True
for i in range(2,n):
    if(n%2==0):
        a=False
if(a==True):
    print("Number is prime")
else:
    print("Number is not prime")
