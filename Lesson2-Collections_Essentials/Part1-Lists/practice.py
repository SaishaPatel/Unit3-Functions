
def filter_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(filter_evens([1,2,3,4,5,6]))
print(filter_evens([10,15,20,25]))
print(filter_evens([1,3,5]))

def list_stats(numbers):
    if numbers:
        new_list = []
        minimum = min(numbers)
        maximum = max(numbers)
        average = round((maximum + minimum) / 2, 2)
        
        new_list.append(f"Maximum: {maximum}")
        new_list.append(f"Minimum: {minimum}")
        new_list.append(f"Average: {average}")
        
        return new_list
    return None

print(list_stats([10,20,30,40]))