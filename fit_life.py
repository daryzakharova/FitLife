# Проект FitLife - MVP версия 1.0

# объявление констант для дальнейших расчётов
WATER_PER_KG = 30
WATER_IN_LITERS = 1000

# запрос данных пользователя
user_name = input('Привет! Введите, пожалуйста, своё имя: ')
user_age = int(input('Введите свой возраст: '))

# запрос данных для расчёта
try:
    user_weight = float(input('Теперь введите свой вес в кг. (пример: 63.5): '))
except ValueError:
    print('Введите вес в кг, используя точку')
 
try:
    user_height = float(input('И Ваш рост в м. (пример: 1.67): '))
except ValueError:
    print('Введите рост в метрах, используя точку')
    
# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# расчёт необходимого количества воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / WATER_IN_LITERS

# отчёт для пользователя
print(f'Привет, {user_name}! Ваш отчет:')
print('-' * 60)
print(f'Ваш возраст: {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('Расчет окончен. Будьте здоровы!')
