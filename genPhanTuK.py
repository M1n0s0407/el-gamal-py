import random


def generate_random_element(p):
    k = random.randint(1, p - 1)
    return k


# Example usage
p = 5311601  # A prime number
k = generate_random_element(p)  # k thuộc Z(p-1)

print("Generated k:", k)
