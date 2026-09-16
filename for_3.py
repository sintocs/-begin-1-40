a = int(input("Введите a"))
b = int(input("Введите b"))
N = 0
for i in range(a+1, b,-1):
     N += 1
     print(i)
     
print(f"Количество: {N}")