def maxProductComposition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            max_product = float('-inf')  # Initialize with negative infinity
            for k in range(len(matrix1[0])):
                max_product = round(max(max_product, matrix1[i][k] * matrix2[k][j]),2)
            row.append(max_product)
        result.append(row)
    return result

# Input fuzzy relation R
m_R = int(input("Enter the number of rows in fuzzy relation R: "))
n_R = int(input("Enter the number of columns in fuzzy relation R: "))
relation_R = []
print("Enter elements of fuzzy relation R row-wise:")
for i in range(m_R):
    row = []
    for j in range(n_R):
        element = float(input(f"Enter element ({i+1},{j+1}): "))
        row.append(element)
    relation_R.append(row)

# Input fuzzy relation S
m_S = int(input("Enter the number of rows in fuzzy relation S: "))
n_S = int(input("Enter the number of columns in fuzzy relation S: "))
relation_S = []
print("Enter elements of fuzzy relation S row-wise:")
for i in range(m_S):
    row = []
    for j in range(n_S):
        element = float(input(f"Enter element ({i+1},{j+1}): "))
        row.append(element)
    relation_S.append(row)

# Perform max-product composition
composition_result = maxProductComposition(relation_R, relation_S)

# Print the result
print("Max-Product Composition:")
for row in composition_result:
    print(row)
