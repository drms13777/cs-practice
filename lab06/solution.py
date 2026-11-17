def count_items(values):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts
def unique_sorted(values: list) -> list:
    return sorted(list(set(values)))
def common(first: list, second: list) -> list:
    return sorted(list(set(first) & set(second)))
def only_in_first(first: list, second: list) -> list:
    return sorted(list(set(first) - set(second)))

a = [1,2,3,3,6,7,8,9,9]
b =[1,2,10]
print(only_in_first(a,b))
print(unique_sorted(a))
print(common(a,b))