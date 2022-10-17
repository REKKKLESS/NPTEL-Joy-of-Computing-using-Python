# Write a program to take string S as an input and replace all vowels by *. Also print the modified string.

# Input
# A string S

# Output
# Modified string

S=input()
v=list('aeiou')
a=""
for i in S:
  if  i.lower() in v:
    a=a+'*'
  else:
    a=a+i
print(a,end="")
