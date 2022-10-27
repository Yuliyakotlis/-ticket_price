ticket = int(input("Введите количество билетов, которые хотите приобрести: "))
total_cost = 0

for i in range(ticket):
    age = int(input("Введите возраст посетителя №" + str(i+1) + ": " ))
    if age >= 18 and age < 25:
       total_cost += 990
    elif age > 25:
       total_cost += 1390
       
if ticket > 3:
    print("Общая стоимость билетов со скидкой 10% составит: " + str(total_cost - (total_cost / 100 * 10)) + " руб.")
else:
    print("Общая стоимость билетов составит: " + str(total_cost) + " руб.")
