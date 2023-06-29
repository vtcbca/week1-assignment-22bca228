#.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

n=input("Enter a number!!:")
if(n.isdigit()):
    b=str(n)
    if(b==b[::-1]):
        print(f"The number {n} is a palindrome number!!")
    else:
        print(f"The number {n} is not a palindrome number!!")

else:
    print(f"The given input {n} is not valid number!!")