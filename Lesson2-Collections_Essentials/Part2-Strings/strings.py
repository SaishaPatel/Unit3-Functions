announcement = " BERGEN TECH robotics meeting TODAY!  "
trimmed = announcement.strip()

# Practice 1
def format_course_code(code):
    # trimmed = code.strip()
    # uppercase_code = trimmed.upper()
    # return uppercase_code
    return code.strip().upper()
print(format_course_code(" webdev101 "))
print(format_course_code(" Python202 "))
print(format_course_code(" Java303 "))

# Practice 2
def count_hashtags(posts):
    count = 0
    words = posts.split()
    for word in words:
        if word.startswith("#"):
            count += 1
    return count
    
post1 = "Great game today! #BergenTech #GoGamrz #Pride"
post2 = "Meeting tomorrow in room 205"
post3 = "#Robotics team withs #StateChampionship! #STEM #BergenTech"

print(count_hashtags(post1))
print(count_hashtags(post2))
print(count_hashtags(post3))

# Example
filename = "assignment.pdf"
print(filename.endswith(".pdf"))
print(filename.endswith(".docs"))