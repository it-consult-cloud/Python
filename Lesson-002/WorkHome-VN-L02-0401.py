# Создать программу которая будет конвертировать значение
# (указанное в метрах и введенное с клавиатуры) в указанную
# пользователем единицу (пользователь вводит это значение с
# клавиатуры, это могут быть мм, см, км)

count = float(input('Введіть число в метрах до конвертування в інші одиниці виміру: '))
EA = input("Введіть код одиниці виміру (1-мм., 2-см., 3-км.): ")

if EA == '1':
    print("Ви вибрали одиницю розрахунку міліметри")
  # c= float(count * 1000)
    print(f'В міліметрах це буде: ', (count * 1000), "мм.")

elif EA == '2':
    print("Ви вибрали одиницю розрахунку сантіметри")
    # c= float(count * 1000)
    print(f'В сантіметрах це буде: ', (count * 100), "см.")

elif EA == '3':
    print("Ви вибрали одиницю розрахунку кілометри")
    # c= float(count * 1000)
    print(f'В кілометрах це буде: ', (count / 1000), "км.")

else:
    print("Ошибка ввода")