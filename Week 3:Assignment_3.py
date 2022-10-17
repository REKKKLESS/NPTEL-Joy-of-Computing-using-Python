# Write a program to count and print the number of odd numbers in a list L.

# Input is managed for you.

# Input:
# A list L

# Output:
# Total number of odd numbers


L = [int(i) for i in input().split()]
odd=[a for a in L if a%2!=0]
print(len(odd),end="")

