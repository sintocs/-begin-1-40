N = int(input("Enter a number (N): "))

total = 0.0  
sign = 1  
for i in range(1, N + 1):
    current_number = 1 + i / 10
    total = total + sign * current_number
    sign = -sign  

print(total)