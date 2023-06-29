#.Write a python script to enter any number and print the sum of its digit.
  
n=int(input("Enter a number:"))
a=n
r=0
sm=0
while(n!=0):
    r=n%10
    sm=sm+r
    n//=10
print(f"The sum of digit of number {a} is {sm}!")  
    