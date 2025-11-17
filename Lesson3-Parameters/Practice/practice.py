# Question 2
def create_card(name, level=1, active=False):
    return {
        "Name": name,
        "Level": level,
        "Active": active
    }
print(create_card("Fireball"))
print(create_card("Shield", level=3, active=True))

# Question 4
def build_profile(username, **stats):
    # Method 1
    # profile = {"username": username}
    # if not stats:
    #     return profile
    # for key, value in stats.items():
    #     profile[key] = value
    # return profile
    
    # My Method
    # dictionary = {"username": username}
    # dictionary.update(stats)
    # return dictionary
    
    # Method 3
    return {"username": username, **stats}

print(build_profile("gamer42", score=850, rank="Gold"))
print(build_profile("player1"))