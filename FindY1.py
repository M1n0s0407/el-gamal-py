def calculate_modulo(alpha, k, p):
    result = pow(alpha, k, p)
    return result

# Example usage
alpha = 2
k = 7
p = 1000003

modulo_result = calculate_modulo(alpha, k, p)
print("y1 =", modulo_result)
