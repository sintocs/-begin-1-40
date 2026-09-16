A = int(input("Enter the starting number (A): "))
B = int(input("Enter the ending number (B): "))
total = 1
for i in range(A, B + 1):
    total = total * i
    print(total)