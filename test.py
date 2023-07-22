import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime():
    while True:
        number = random.randint(10**6, 10**7 - 1)  # Generate a random 7-digit number
        if is_prime(number):
            return number

# Example usage
prime_number = generate_prime()
print("Random 7-digit prime number:", prime_number)
