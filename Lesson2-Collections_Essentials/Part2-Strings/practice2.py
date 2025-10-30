# Question 3: Code Writing
# def format_phone_number(phone):
#     phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
#     if len(phone) == 10 and phone.isdigit():
#         return(f"({phone[0,1,2]}) {phone[3,4,5]}-{phone[6,7,8,9]}")
#     return "Invalid phone number"
# format_phone_number(print("555-123-4567"))
# format_phone_number(print("(555) 123 4567"))
# format_phone_number(print("5551234567"))
# format_phone_number(print("123"))

# Alternative Solution
def format_phone_number(phone):
    cleaned = ""
    for ch in phone:
        if ch.isdigit():
            cleaned += ch
    if not len(cleaned) == 10:
        return "Invalid phone number"
    area = cleaned[:3]
    middle = cleaned[3:6]
    list = cleaned[6:]
    return f"(({area}) {middle}-{list})"
format_phone_number(print("555-123-4567"))
format_phone_number(print("(555) 123 4567"))
format_phone_number(print("5551234567"))
format_phone_number(print("123"))