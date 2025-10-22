# 3
def calculate_discount(price, member_status):
    if member_status == "premium":
        return price * 0.7
    elif member_status == "standard":
        return price * 0.85
    else:
        return price

print(calculate_discount(100, "premium"))

# 6
def count_vowels(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

print(count_vowels("AEIOU"))

#  9
def validate_password(password):
    if len(password) < 8:
        return False
    has_digit = False
    for char in password:
        if "0" <= char <= "9":
            has_digit = True
    return has_digit
print(validate_password("Hello123"))