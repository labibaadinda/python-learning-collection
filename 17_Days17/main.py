# constructor -> part blueprint that allows us to specify what should happen
# this is also known in programming as initializing an object
# when object being initialized, we can set variables or counters to they're starting values
# the way that we would create the constructor is by using a special function, which is the init function
# you can tell it's special because it isn't just the def keyword and then the name of the function. it is got two underscores
# and this means that it's a method that the Python interpreter knows about and knows that it has a special function

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

# method itu ga kaya fungsi biasa, dia selalu butuh parameter self dan ini auto build dari python interpreternya
    def follow(self, user):
        self.following += 1
        user.followers += 1

# attributes are things that the object has
# method are the things that the object does
# method, method nya itu inside the class declaration, we have function, but remember when a function is attached to object itu disebut method


# user1 = User(10, "dinda")
# print(user1.id)
# user1.followers = 12
# print(user1.followers)

user_1 = User("1", "angela")
user_2 = User("2", "jack")

user_2.follow(user_1)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)


