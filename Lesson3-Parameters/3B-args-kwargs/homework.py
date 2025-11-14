# Question 1 - Code Writing (*args)
def combine_values(*values):
    if not values:
        return 1
    product = 1
    for value in values:
        product *= value
    return product
print(combine_values(2,3,4))
print(combine_values(5))
print(combine_values())

# Question 2 - Code Writing (**kwargs)
def merge_details(label, **info):
    details = {"Label": label}
    details.update(info)
    return details
print(merge_details("ItemA", size="Large", cost=12.50))
print(merge_details("UserX"))

# Question 3 - Code Tracing
# 8 
# 10
# 0

# Question 4 - Code Tracing
# {"name": "Alpha", "x": "1", "y": 2, "count": 2}
# {"name": "Beta", "count": 0}