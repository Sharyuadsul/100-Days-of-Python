# file = open("demo.txt")
# content = file.read()
# print(content)
# file.close()

with open("demo.txt", mode="a") as file:
    #content = file.read()
    file.write("\ngand marao")

