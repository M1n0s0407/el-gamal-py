import random


def generate_private_key(p):
    while True:
        a = random.randint(2, p - 2)
        if gcd(a, p - 1) == 1:
            return a


# Euclidean algorithm to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Example usage
p = 5311601  # A prime number
a = generate_private_key(p)

print("Generated a:", a)
