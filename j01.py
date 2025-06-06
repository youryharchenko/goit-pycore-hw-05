import sys
import re

def caching_fibonacci():
    # Словник для кешування
    cache = {}
    # Рекурчивна функція обчислення чисел Фібоначі з кешуванням
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    # Повертаємо функціональне замикання
    return fibonacci
        
if __name__ == "__main__":
    # Перевіряємо чи передано параметр і, що він є числом
    if len(sys.argv) == 2 and re.match(r"^[+-]?\d+$", sys.argv[1]):
        # Якшо папаметр є і він коректний, то створюємо функцію з кешуванням результатів 
        fib = caching_fibonacci()
        # Берем параметр як ціле, обчислюємо число Фібоначі та виводимо результат
        n = int(sys.argv[1])
        print(f"fib({n}) -> {fib(n)}")
    else:
        # Інакше виводимо повідомлення
        print("Має бути передано один параметр: ціле число")




