price = float(input("Введите цену товара: "))

for i in range(1, 11):
    kg = i / 10
    total_price = price * kg
    print(f"Цена за {kg} кг: {total_price:.2f}")