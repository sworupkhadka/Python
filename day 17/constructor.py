# Class = blueprint for objects
class User:
    # __init__ = runs when object is made
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method for following another user
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create users
user_1 = User("001", "Angela")
user_2 = User("002", "Angelo")

# user_1 follows user_2
user_1.follow(user_2)

# Print results
print(user_1.id, user_1.username)
print(user_2.id, user_2.username)


print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
