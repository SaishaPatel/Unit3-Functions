# Question 2: Code Writing
def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    top_players = []
    for player in players:
        if player["score"] >= min_score:
            top_players.append(player["username"])
    return top_players
# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing']

# Question 3: Code Tracing
# Output:
#       Total songs: 9
#       First Song: EYE OF THE TIGER
#       Last Song: BLINDING LIGHTS

# Question 4: Code Writing
def calculate_cart_total(cart):
    ''' Calculate the total cost of all items in the cart and returns: total cost (float)'''
    total_price = 0
    for object in cart:
        price = object["price"] * object["quantity"]
        total_price += price
    return total_price

# Test it
cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")