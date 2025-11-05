# Question 1 - Code Tracing
# {"key_a": "value1", "key_b": 150, "key_d": 50}
# False

# Question 2 - Code Tracing
# 120
# 60.0 (float value)

# Question 3 - Code Writing
def get_user_bio(user):
    for key, value in user.items():
        if key == "bio":
            return value
    return "No bio available"
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))
print(get_user_bio({"username": "newbie"}))

# Question 4 - Code Tracing
# 60
# 160

# Question 5 - Code Tracing
# 2

# Question 6 - Code Writing
def get_total_engagement(post):
    sum = 0
    if not "likes" in post:
        post["likes"] = 0
    if not "comments" in post:
        post["comments"] = 0
    if not "shares" in post:
        post["shares"] = 0
    
    sum += post["likes"] + post["comments"] + post["shares"]
    return sum

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))
print(get_total_engagement({"likes": 50, "comments": 5}))
print(get_total_engagement({"views": 1000}))

# Question 7 - Code Tracing
# 3
# 3

# Question 8 - Code Tracing
# {"key1": "value1", "key2": 200, "key3": 50} 
# {"key1": "value1", "key2": 100, "key4": True} 

# Question 9 - Code Writing
def find_most_followed(users):
    max_followers = 0
    most_followed = users[0]["username"]
    if users:
        for user in users:
            if user["followers"] > max_followers:
                max_followers = user["followers"]
                most_followed = user["username"]
        # return max_followers
        return most_followed
    return None

users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000}
]

print(find_most_followed(users))