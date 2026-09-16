price = float(input("Введите цену товара: "))
for kg in range(1, 11):
    total_price = price * kg
    print(f"Цена за {kg} кг: {total_price:.2f}")