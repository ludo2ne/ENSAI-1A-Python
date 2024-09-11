a = 2
b = 8

print("a = ", a)
print("b = ", b)

print("-" * 50)
print("Sans utiliser de variable temporaire")
print("-" * 50)

a = a + b
b = a - b
a = a - b

print("a = ", a)
print("b = ", b)


print("-" * 50)
print("Multi affectation")
print("-" * 50)

a, b = b, a

print("a = ", a)
print("b = ", b)
