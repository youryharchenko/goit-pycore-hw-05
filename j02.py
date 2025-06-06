import sys
import re

def generator_numbers(text: str):
    # Розбиваємо рядок пробілами, вибираємо числа та формуємо список float
    numbers = [float(token.strip()) for token in text.split(" ") if re.match(r"\s?(\d+\.?\d*)\s?", token)]
    # Генеруємо
    for n in numbers:
        yield n

def sum_profit(text: str, generator) -> float:
    # Обчислюємо суму генерованих чисел 
    return sum(generator(text))

def main(source: str):
   print(f"Вхідний рядок: {source}\nСума: {sum_profit(source, generator_numbers)}")

if __name__ == "__main__":
    # Перевіряємо чи передано параметр 
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        # Інакше виводимо повідомлення
        print("Має бути передано один параметр: рядок з текстом та числами")