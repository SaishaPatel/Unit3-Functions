# Question 2: Create Card Function
def create_card(name, level=1, active=False):
    return {
        "Name": name,
        "Level": level,
        "Active": active
    }

# Test Question 2
print(create_card("Fireball"))  # Should return: {'name': 'Fireball', 'level': 1, 'active': False}
print(create_card("Shield", level=3, active=True))  # Should return: {'name': 'Shield', 'level': 3, 'active': True}

# Question 4: Build Profile Function
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

# Test Question 4
print(build_profile("gamer42", score=850, rank="Gold"))  # Should return: {'username': 'gamer42', 'score': 850, 'rank': 'Gold'}
print(build_profile("player1"))  # Should return: {'username': 'player1'}

# Question 5 - Code Tracing
# 18.0
# 15.0

# Question 6:
def make_notification(user, *messages, urgent=False):
    text = ", ".join(messages)
    urgency = "URGENT: " if urgent else ""
    return f"{urgency}{user} - {text}"

# Test Question 6
print(make_notification("admin", "Server down!", urgent=True))  # Should return: "URGENT: admin - Server down!"
print(make_notification("user", "Welcome", "Check inbox"))  # Should return: "user - Welcome, Check inbox"

# Question 7 - Code Tracing
# SELECT name, email FROM users LIMIT 10
# SELECT * FROM logs WHERE level='error' LIMIT 5

# Question 8: Log Action Function
def log_action(actor, *actions, timestamp=None, **context):
    text = ", ".join(actions)
    context_list = []
    for key, value in context.items():
        context_string = (f"{key}={value}")
        context_list.append(context_string)
    context_text = ", ".join(context_list)
    return f"{actor}: {text} | {context_text}"

# Test Question 8
print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))  # Should return: "bot: login, scan | source=API, ip=1.2.3.4"