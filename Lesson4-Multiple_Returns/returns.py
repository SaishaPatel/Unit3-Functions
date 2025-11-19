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

# Multiple Returns - Python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter # Turns into a tuple (area, perimeter)
result = calculate_room(10, 5)
print(result)
print(type(result))

print(type(42)) # int
print(type(42,)) # tuple for single item
no_parentheses = 1,2,3
print(type(no_parentheses))

# Unpacking tuple
area_result, perimeter_result = calculate_room(20,6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

# Practice 1: Student Grade Analyzer
def grade_statistics(grades):
    # if not grades:
    #    return 0,0,0,False
    # average = sum(grades) / len(grades)
    # highest = 0
    # lowest = 100
    # for grade in grades:
    #     if grade > highest:
    #         highest = grade
    #     if grade < lowest:
    #         lowest = grade
    # if average >= 60:
    #     passed = True
    # return average, highest, lowest, passed
    if not grades:
        return 0,0,0,False
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 60
    
    return average, highest, lowest, passed
    
print(grade_statistics([85,92,78,90]))
print(grade_statistics([]))
print(grade_statistics([80,80,80]))