def cartesianProduct(fuzzy_set1, fuzzy_set2):
    result = {}
    for key1, value1 in fuzzy_set1.items():
        for key2, value2 in fuzzy_set2.items():
            result[(key1, key2)] = min(value1 ,value2)
    return result

# Input fuzzy set A
n_A = int(input("Enter the number of elements in fuzzy set A: "))
fuzzy_set_A = {}
for i in range(n_A):
    key_A = input(f"Enter key {i+1} of fuzzy set A: ")
    value_A = float(input(f"Enter membership degree for {key_A}: "))
    fuzzy_set_A[key_A] = value_A

# Input fuzzy set B
n_B = int(input("Enter the number of elements in fuzzy set B: "))
fuzzy_set_B = {}
for i in range(n_B):
    key_B = input(f"Enter key {i+1} of fuzzy set B: ")
    value_B = float(input(f"Enter membership degree for {key_B}: "))
    fuzzy_set_B[key_B] = value_B

# Calculate Cartesian product
cartesian_product = cartesianProduct(fuzzy_set_A, fuzzy_set_B)

print("Cartesian Product:")
for pair, value in cartesian_product.items():
    print(pair, ":", value)
