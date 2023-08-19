def calculate_modulo(alpha, a, p):
    result = pow(alpha, a, p)
    return result


# Example usage
alpha = 3
a = 1132643
p = 5311601

modulo_result = calculate_modulo(alpha, a, p)
print("α^a mod p =", modulo_result)
