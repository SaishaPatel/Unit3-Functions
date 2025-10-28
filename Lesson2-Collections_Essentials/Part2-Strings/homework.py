# Question 1: Code Tracing
# Output: john.smith gmail.com

# Question 2: Code Tracing
# Output: tqbf

# Question 3: Code Writing - Extract Domain
def extract_domain(email):
    if "@" in email and email.count("@") == 1:
        domain = email.lower().split("@")[1]
        return domain
    return "Invalid email"
print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))

# Question 4: Code Tracing
# Output: 123456

# Question 5: Code Tracing
# Output: MY_DOCUMENT

# Question 6: Code Tracing
# Output: banana

# Question 7: Code Writing - Filter Numbers
def filter_numbers(text):
    filtered = ""
    for char in text:
        if not char.isdigit():
            filtered += char 
    return filtered
print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))

# Question 8: Code Tracing
# Output: https://example.com/users/profile

# Question 9: Code Writing - Count Characters
def count_character_types(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if "A" <= char <= "Z" or "a" <= char <= "z":
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1
    return {
        "letters": letters, 
        "digits": digits, 
        "spaces": spaces
    }
print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))