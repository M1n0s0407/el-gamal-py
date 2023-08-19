def calculate_modulo(y2, y1, a, p):
    inverse = pow(y1, a, p)  # Calculate the inverse of y1^a mod p
    result = (y2 * pow(inverse, -1, p)) % p  # Calculate (y2 * (y1^a)^(-1)) mod p
    return result


# Example usage
y2 = 761383
y1 = 4591509
a = 1132643
p = 5311601

modulo_result = calculate_modulo(y2, y1, a, p)
print("Result =", modulo_result)
