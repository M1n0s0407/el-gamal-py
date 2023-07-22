def is_primitive_element(alpha, p):
    for i in range(1, p-1):
        if pow(alpha, i, p) == 1:
            return False
    return True

def find_alpha(p):
    for alpha in range(2, p):
        if is_primitive_element(alpha, p):
            return alpha
    return None

# Example usage
p = 1000003
alpha = find_alpha(p)

if alpha is None:
    print("No primitive element (alpha) found for p =", p)
else:
    print("Primitive element (alpha) for p =", p, "is", alpha)
