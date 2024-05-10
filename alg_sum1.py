def algSum(*args):
    r = {}
    for i in args[0].keys():
        r[i] = round(round(args[0].get(i, 0) + args[1].get(i, 0), 2) - round(args[0].get(i, 0) * args[1].get(i, 0), 2), 2)
    return r

n = int(input("Enter the number of elements in each fuzzy set: "))
fuzzy_sets = []
for i in range(2):
    fuzzy_set = {}
    for j in range(n):
        key = input(f"Enter key {j+1} of fuzzy set {i+1}: ")
        value = float(input(f"Enter value {j+1} of fuzzy set {i+1}: "))
        fuzzy_set[key] = value
    fuzzy_sets.append(fuzzy_set)

print("Algebraic Sum:", algSum(*fuzzy_sets))
