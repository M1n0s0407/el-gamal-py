def calculate_modulo(alpha, k, p):
    result = pow(alpha, k, p)
    return result


# Example usage
alpha = 3
k = 3511415
p = 5311601

modulo_result = calculate_modulo(alpha, k, p)
print("y1 =", modulo_result)
