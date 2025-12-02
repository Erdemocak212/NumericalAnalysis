def remove_duplicates(seq: list) -> list:
   
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result


def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict

print(calculate_pyramid_height(10))     
print(remove_duplicates([1,2,2,3,1]))   
print(list_counts(["a","b","a"]))       
print(reverse_dict({"x":1, "y":2}))    
