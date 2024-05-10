def complement(fuzzy_set):
    result = {}
    for key, value in fuzzy_set.items():
        result[key] = round(1 - value, 2)
    return result

n = int(input("Enter the number of elements in the fuzzy set: "))
fuzzy_set = {}
for i in range(n):
    key = input(f"Enter key {i+1} of the fuzzy set: ")
    value = float(input(f"Enter membership degree for {key}: "))
    fuzzy_set[key] = value

print("Original Fuzzy Set:", fuzzy_set)
print("Complement of Fuzzy Set:", complement(fuzzy_set))
