# lis = [1, 2, 3, 4, 5]
# new_lis = [n+1 for n in lis]
# print(new_lis)

# name = "djbcaudjcn"
# letters = [letter for letter in name]
# print(letters)


# new_list = [item*2 for item in range(1,5)]
# print(new_list)


#conditional list comprehension
names= ["john", "carolina", "smith", "conner", "lily"]
small_names = [name for name in names if len(name)<=5]
large_names = [name.upper() for name in names if len(name)>5]
print(small_names)
print(large_names)