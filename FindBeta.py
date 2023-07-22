def calculate_modulo(alpha, a, p):
    result = pow(alpha, a, p)
    return result

# Example usage
alpha =2 
a = 111115
p = 1000003

modulo_result = calculate_modulo(alpha, a, p)
print("α^a mod p =", modulo_result)
