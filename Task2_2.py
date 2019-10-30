print("2.2.1 Product of multiplication: ")
a = 1692
mul = 1
while (a>1):
    mul = mul * (a % 10)
    a = int(a / 10)
print(mul)

print("\n2.2.2 Reversed number: ")
a = 1692
print(str(a))
print(str(a)[::-1])

print("\n2.2.3 Ascending order: ")
a = 1692
ascend = "".join(sorted(str(a)))
print(ascend)

