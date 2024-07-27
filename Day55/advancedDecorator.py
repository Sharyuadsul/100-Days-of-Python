class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function

@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")

user = User("Sharyu")
user.is_logged_in =True
create_blog_post(user)
