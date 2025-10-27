# 1: Remove Duplicates
def remove_duplicates(items):
    removed_list = []
    for item in items:
        if not (item in removed_list):
            removed_list.append(item)
    return removed_list

# result = remove_duplicates([1,2,2,3,1,4])
# result = remove_duplicates(["a", "b", "a", "c"])
# result = remove_duplicates([5,5,5])
result = remove_duplicates([])
print(result)

# 2: Common Numbers
def find_common(list1, list2):
    common_list = []
    for item in list1:
        if item in list2:
            if not(item in common_list):
                common_list.append(item)
    return common_list

# result = find_common([1,2,3], [2,3,4])
# result = find_common(["a", "b"], ["c", "c"])
# result = find_common([1,1,2], [2,2,3])
result = find_common([], [1,2])
print(result)

# 3: Reverse Sublists
def reverse_sublists(data, size):
    modified_list = []  
    for i in range(0, len(data), size):
        chunk = data[i:i+size]
        reversed_chunk = chunk[-1::-1]
        modified_list += reversed_chunk
    return modified_list
# result = reverse_sublists([1,2,3,4,5,6], 2)
# result = reverse_sublists([1,2,3,4,5], 3)
# result = reverse_sublists([1,2,3,4], 1)
result = reverse_sublists([1,2,3], 5)
print(result)

# 4: Rotate List
def rotate_list(items, positions):
    if not items:
        return []
    rotated_list = []
    rotated_list += items
    if positions > 0:
        count = 0
        while count < positions:
            last_item = rotated_list.pop()
            rotated_list.insert(0,last_item)
            count += 1
    if positions < 0:
        count = 0
        while count < positions*-1:
            first_item = rotated_list.pop(0)  
            rotated_list.append(first_item)
            count += 1
    return rotated_list
# result = rotate_list([1,2,3,4,5], 2)
# result = rotate_list([1,2,3,4,5], -2)
# result = rotate_list([1,2,3], 0)
result = rotate_list([1,2,3], 5)
print(result)