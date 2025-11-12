# Question 1: Code Tracing
# [26]

# Question 2: Code Tracing
# NEXUS

# Question 3: MVP Calculator
def match_mvp(players):
    highest_ratio = 0
    highest_player = ""
    for player, value in players.items():
        ratio = value["kills"] / value["deaths"]
        if ratio > highest_ratio:
            highest_ratio = ratio
            highest_player = player
    return highest_player

players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}
print(match_mvp(players))