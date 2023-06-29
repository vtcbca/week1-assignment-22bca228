#7.Write a python script to enter any string, replace vowel with its position number.
#For Example: input: Amit
#             output:0m2t

s=input("Enter a string:")
v=''
m=('a','e','i','o','u','A','E','I','O','U')
for index,j in enumerate(s):
    if(j in m):
        v+=str(index)
    else:
        v+=j
    
print(f"The string '{s}' after change is '{v}' ")