# SCOPE - The visibility of variables, where it can be seen and used
# GLOBAL - outside all functions
# LOCAL - inside a function(only visible there)

# THE BUG - CRASHES (UnboundLocalError)
def add_bonus():
    score = score + 100 # = Python thinks it's local

score = 500
add_bonus()