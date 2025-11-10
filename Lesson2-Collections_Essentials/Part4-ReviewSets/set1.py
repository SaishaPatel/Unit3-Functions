# Question 1: Code Tracing
# 2300

# Question 2: Code Tracing
# WOW WOW LFG

# Question 3: Code Writing
def find_top_donor(donations):
    highest_value = 0
    highest_name = ""
    for key, value in donations.items():
        if value > highest_value:
            highest_value = value
            highest_name = key
    return highest_name
        

donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}
print(find_top_donor(donations))