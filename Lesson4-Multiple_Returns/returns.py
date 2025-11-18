def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

# 1. Return Type: None -> "No Value"
# Meaning: Absence of value, not set, not found
# Use For: Missing Data, search failurs, optional parameters
result = None
print(result is None) # True - identity check
print(result == None) # True - equality check
print(not result)     # True - falsy check

# 2. Return Type: False = Boolean False
# Meaning: Explicit false condition, validation failure, negative result
# Use For: Validation result, boolean operations, success/failures status
result = False
print(result is False) # True - identity check
print(not result)      # True - boolean negation
print(result == 0)     # True - falsy check

# 3. Return Zero - A Valid Number
# Zero is VALID numeric value, not absence of value!
result = 0
print(result == 0)      # True - numeric equality
print(not result)       # True - falsy in boolean context
print(result is None)   # False - Different objects
print(result is False)  # False - Different types
