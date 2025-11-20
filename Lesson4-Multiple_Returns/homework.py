# Question 1
def search_user_database(query):
    if query == "" or query.strip() == "": # Checks is empty or if empty when spaces are rmeoved
        return None, "No search query", False
    if not query.isalpha(): # Checks if there are only letters
        return False, "Invalid characters", False
    if query == "john":
        return 3, "Found 3 users", True # User found
    return 0, "No users found", True # Valid search, but john is not found

result, message, success = search_user_database("")
print(result)
print(message)
print(success)

result, message, success = search_user_database("   ")
print(result)
print(message)
print(success)

result, message, success = search_user_database("user123")
print(result)
print(message)
print(success)

result, message, success = search_user_database("user@gmail")
print(result)
print(message)
print(success)

result, message, success = search_user_database("admin")
print(result)
print(message)
print(success)

result, message, success = search_user_database("john")
print(result)
print(message)
print(success)

# Question 2
def analyze_book_pages(pages):
    if not pages: 
        return 0, 0, 0.0, False # Handles empty list
    total_books = len(pages)
    total_pages = sum(pages)
    average = total_pages / total_books
    over_500 = max(pages) > 500
    return total_books, total_pages, average, over_500

total_books, total_pages, average, over_500 = analyze_book_pages([501, 400, 300])
print(total_books)
print(total_pages)
print(average)
print(over_500)

total_books, total_pages, average, over_500 = analyze_book_pages([500, 400, 300])
print(total_books)
print(total_pages)
print(average)
print(over_500)

total_books, total_pages, average, over_500 = analyze_book_pages([])
print(total_books)
print(total_pages)
print(average)
print(over_500)

total_books, total_pages, average, over_500 = analyze_book_pages([200, 150, 300])
print(total_books)
print(total_pages)
print(average)
print(over_500)

total_books, total_pages, average, over_500 = analyze_book_pages([250, 180, 620, 310])
print(total_books)
print(total_pages)
print(average)
print(over_500)

    