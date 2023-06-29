##5.Write a python script to enter any string and count vowel.

s=input("Enter a string:")
a=('a','e','i','o','u','A','E','I','O','U')
v=0
for i in s:
    if i in a:
        v+=1
print(f"The vowels count in '{s}' is {v}")
    