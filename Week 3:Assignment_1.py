# There is list L containing some numbers. Write a program to create a new list which contains the numbers which are either divisible by 5 or 7 or both. Print that new list in ascending order.

# Input is already managed for you.

# Input:
# A list L
# Output: A new list P

# Example
# Input:
# L = [7, 8, 9, 10, 11]

# Output:
# [7, 10]

# Solution:

L = [int(i) for i in input().split()]
ans=[z for z in L if z%5==0 or z%7==0]
print(sorted(ans),end="")
