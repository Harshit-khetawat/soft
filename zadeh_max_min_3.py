def cartesianPdt(f1, f2):
    """
    Calculate the Cartesian product of two fuzzy sets.
    """
    pdt = []
    for key1, value1 in f1.items():
        p = []
        for key2, value2 in f2.items():
            val = min(value1, value2)
            p.append(val)
        pdt.append(p)
    return pdt

# Input for first fuzzy set (A)
n1 = int(input("Enter the number of elements in the  fuzzy set A: "))
fuzzy_set_A = {}
a_bar = {}  # Complement of fuzzy set A
for i in range(n1):
    key = input(f"Enter key {i+1} of fuzzy set A: ")
    value = float(input(f"Enter value {i+1} of fuzzy set A: "))
    fuzzy_set_A[key] = value
    a_bar[key] = round(1 - value, 2)

# Input for second fuzzy set (B)
n2 = int(input("Enter the number of elements in the  fuzzy set B: "))
fuzzy_set_B = {}
# Universal fuzzy set Y with membership degree 1
for i in range(n2):
    key = input(f"Enter key {i+1} of fuzzy set B: ")
    value = float(input(f"Enter value {i+1} of fuzzy set B: "))
    fuzzy_set_B[key] = value
    
n3 = int(input("Enter the number of elements in the fuzzy set C :"))
fuzzy_set_C={}
for i in range(n3):
    key = input(f"Enter key{i+1} of fuzzy set C :")
    value = float(input(f"Enter value{i+1} of fuzzy set C : "))
    fuzzy_set_C[key] = value


# Calculating (A x B)
cartesian_A_B = cartesianPdt(fuzzy_set_A, fuzzy_set_B)
print("\n(A x B) is:")
for row in cartesian_A_B:
    print(row)

# Calculating (A' x Y)
cartesian_A_complement_C = cartesianPdt(a_bar, fuzzy_set_C)
print("\n(A' x C) is:")
for row in cartesian_A_complement_C:
    print(row)

# Calculating union
union = []
for i in range(len(cartesian_A_B)):
    u1 = []
    for j in range(len(cartesian_A_B[0])):
        val = max(cartesian_A_B[i][j], cartesian_A_complement_C[i][j])
        u1.append(val)
    union.append(u1)

print("\n(A x B) V (A' x C) =")
for row in union:
    print(row)
