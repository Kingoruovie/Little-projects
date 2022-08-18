class User:
    """creates users of a particular platform"""
    def __init__(self, user_id, user_name, follower=0, following=0):
        self.id = user_id
        self.name = user_name
        self.follower_counts = follower
        self.following_count = following

    def follow(self, user):
        user.follower_counts += 1
        self.following_count += 1


user_1 = User("007", "Ovie")
user_2 = User("oo2", "Dozie")

user_1.follow(user_2)

print(user_1.follower_counts)
print(user_1.following_count)
print(user_2.follower_counts)
print(user_2.following_count)
