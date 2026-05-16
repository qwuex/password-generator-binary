import random

letter = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzCcVvBbNnMm"
symbols = "!@#$%^&*()_-+="
digitals = "1234567890"
pool = ""

use_digitals = input("Add digits? (да/нет): ").lower()
use_symbols = input("Add symbols? (да/нет): ").lower()

pool = pool + letter
if use_digitals == "да":
    pool = pool + digitals
if use_symbols == "да":
    pool = pool + symbols

number = int(input("Количество паролей?\n"))
length = int(input("Длина пароля?\n"))

print("\n--- Результаты генерации ---")

for i in range(number):
    password = ""
    for j in range(length):
        password += random.choice(pool)
    
    # Переводим текущий пароль в двоичный код
    binary_password = ""
    for char in password:
        binary_char = bin(ord(char))[2:]
        binary_password += binary_char + " "
        
    # Выводим оба варианта для наглядности
    print(f"Пароль №{i+1}: {password}")
    print(f"В двоичном коде: {binary_password}\n")
