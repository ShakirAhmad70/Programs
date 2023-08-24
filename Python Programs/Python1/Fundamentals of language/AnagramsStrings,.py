s1 = input("Enter First String:")
s2 = input("Enter Second String:")

if sorted(s1) == sorted(s2):
    print("These are the anagrams strings")
else:
    print("These are not the anagrams strings")