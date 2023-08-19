def calculate_modulo(x, beta, k, p):
    result = (x * pow(beta, k, p)) % p
    return result


# Example usage
x = 75
beta = 4575961
k = 3511415
p = 5311601

modulo_result = calculate_modulo(x, beta, k, p)
print("y2 =", modulo_result)
