class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


new_user = User("001", "Jon")
new_user2 = User("002", "Sam")

new_user.follow(new_user2)

# print(new_user.id)
print(new_user.followers)
print(new_user.following)
print(new_user2.followers)
print(new_user2.following)