#  Question 3
def create_username(first_name, last_name):
    combined = f"{first_name}_{last_name}".lower()
    return combined
print(create_username("John", "Smith"))
print(create_username("MARY", "Jones"))
print(create_username("Alex", "TAYLOR"))

# Question 6
def check_email(email):
    if "@" in email and email.lower().endswith(".com"):
        return True
    return False
# Alternative
# def check_email(email):
#    email_lower = email.lower()
#    return "@" in email_lower and email_lower.endswith(".com")
print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))
print(check_email("invalid.com"))
print(check_email("test@school.com"))

# Question 9
def create_slug(title):
    slug = title.strip().lower().replace(" ", "-")
    return slug
print(create_slug("My First Blog Post"))
print(create_slug(" Python Tutorial "))
print(create_slug("Web Development 101"))