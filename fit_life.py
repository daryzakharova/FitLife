# Проект FitLife - MVP версия 1.0

# запрос данных пользователя
user_name = input('Привет! Введите, пожалуйста, своё имя: ')
user_age = int(input('Введите свой возраст: '))

# запрос данных для расчёта
try:
    user_weight = float(input('Теперь введите свой вес (кг.): '))
except ValueError:
    print('Введите вес в кг, используя точку')

try:
    user_height = float(input('И Ваш рост (м.): '))
except ValueError:
    print('Введите рост в метрах, используя точку')

# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# расчёт необходимого количества воды
water_ml = user_weight * 30
water_l = water_ml / 1000

# отчёт для пользователя
print(f'Привет, {user_name}! Ваш отчет:')
print('-' * 60)
print(f'Ваш возраст: {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')