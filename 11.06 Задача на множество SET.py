# машины
# фруктами
# красными предметами

# ["ferrari", "porhse", "ford", "lada"]
# ["гранат", "банан", "арбуз", "персик"]
# ["ferrari", "ford", "гранат"]


# 1. красные машины
# 2. НЕ красные фрукты

# объединение
# не красные фруты

cars = {"ferrari", "porhse", "ford", "lada"}
fruits = {"гранат", "банан", "арбуз", "персик"}
red_stuf = {"ferrari", "ford", "гранат"}

print(cars & red_stuf)

print(fruits - red_stuf)

