class User:
    def __init__(self,id,name):
        self.user_id = id
        self.username = name
        self.followers = 0

user_1 = User(12, "shar")
print(user_1.followers)
