N = int(input("Enter a number (N): "))
total = 1.0
for i in range(1, N + 1):
    total = total * (1 + i * 0.1)
    print(total)
