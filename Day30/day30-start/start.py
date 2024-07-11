#FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dict = {"key": "value"}
# value = a_dict["kkhfsajdv"]

# IndexError
# a_list =  ["a", "b", "c"]
# var = a_list[4]

# TypeError
# text = "aa"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["kkhfsajdv"])
# except FileNotFoundError:
#     file = open("a_file.text", "w")
#     file.write("exception handled")
# except KeyError:
#     print(f"The Key does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

# finally:
#     raise TypeError("this is an error that i ade up")


height=float(input("height: "))
weight =int(input("Weight: "))

if height>3:
    raise ValueError("The human height should not be over 3 meters")

bmi = weight / height **2
print(bmi)