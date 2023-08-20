from sympy.ntheory import primitive_root

p = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000237
primitive_element = primitive_root(p)

print(f"The primitive element of {p} is {primitive_element}")
