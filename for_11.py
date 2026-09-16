N = int(input("Enter a number (N): "))
total = 0
for i in range(N, 2 * N + 1):
    total = total + i ** 2
    print(total)