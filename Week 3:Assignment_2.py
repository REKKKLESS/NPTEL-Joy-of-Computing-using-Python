# Write a function rev which takes a list L and integer n and print the first n largest numbers of the list.

# Input is managed for you, please write the required function only.

# Input:
# A list L and an integer n.

# Output:
# First n largest numbers

def rev(L,n):
  print(sorted(L)[::-1][:n],end="")
