def boundedSum(*args):
    result = {}
    for key in args[0].keys():
        result[key] = min(1, args[0].get(key, 0) + args[1].get(key, 0))
    return result

n = int(input("Enter the number of elements in each fuzzy set: "))
fuzzy_sets = []
for i in range(2):
    fuzzy_set = {}
    for j in range(n):
        key = input(f"Enter key {j+1} of fuzzy set {i+1}: ")
        value = float(input(f"Enter value {j+1} of fuzzy set {i+1}: "))
        fuzzy_set[key] = value
    fuzzy_sets.append(fuzzy_set)

print("Bounded Sum:", boundedSum(*fuzzy_sets))
