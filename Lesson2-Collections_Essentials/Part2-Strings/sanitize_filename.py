# Solution 1
# def sanitize_filename(filename):
#     clean = filename.lower().replace(" ", "_")
#     allowed = ""
#     for char in clean:
#         if char.isalnum() or char in ".-_":
#             allowed += char
#     if allowed.endswith(".txt"):
#         result = allowed
#     else:
#         if "." in allowed:
#             dot_pos = allowed.rfind(".")
#             allowed = allowed[:dot_pos]
#         result = allowed + ".txt"
#     if len(result) > 50:
#         max_base = 50-4
#         result = result[:max_base] + ".txt"
#     return result

# print(sanitize_filename("Ancient Scroll.txt"))
# print(sanitize_filename("Quest 2042! (Epic)"))
# print(sanitize_filename("notes"))
# print(sanitize_filename("X"*60))

# Solution 2
def sanitize_filename(filename):
    clean = filename.lower().replace(" ", "_")
    safe = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            safe += char
    if not safe.endswith(".txt"):
        if "." in safe:
            safe = safe[:safe.rfind(".")]
        safe += ".txt"
    if len(safe) > 50:
        safe = safe[:46] + ".txt"
    return safe

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X"*60))
 