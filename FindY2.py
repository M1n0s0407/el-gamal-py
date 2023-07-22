def calculate_modulo(x, beta, k, p):
    result = (x * pow(beta, k, p)) % p
    return result

# Example usage
x = 113
beta = 7673
k = 7
p = 1000003

modulo_result = calculate_modulo(x, beta, k, p)
print("y2 =", modulo_result)
