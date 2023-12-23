print()

number=(int(input(" Enter 4-digit number = ")))
n1 = print(number // 1000)
n2 = print(number //100 % 10)
n3 = print(number //10 % 10)
n4 = print(number % 10)

result = n1 + n2 + n3 + n4

print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
print(f"Result: {result}")
