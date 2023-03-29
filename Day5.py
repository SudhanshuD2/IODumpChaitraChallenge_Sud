# CODE
n = int(input("Enter nth number:"))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum of first {} numbers: ".format(n), sum)

# INPUT and OUTPUT
# Enetr nth number: 5
# Sum of first 5 numbers: 15
