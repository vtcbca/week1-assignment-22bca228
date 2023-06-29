#6.Write a python script to enter any string and print only part of string. Take input of start character and end character from user.


s=input("Enter a string:")
t=int(input("Enter start position:"))
e=int(input("Enter end position:"))
    
print(f"The part of the string '{s}' is '{s[t-1:e:]}'")
