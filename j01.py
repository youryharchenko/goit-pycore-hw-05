import sys
import re

def caching_fibonacci():
    cache = {}

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
        
    return fibonacci
        
if __name__ == "__main__":
    if len(sys.argv) == 2 and re.match(r"^[+-]?\d+$", sys.argv[1]):
        fib = caching_fibonacci()
        n = int(sys.argv[1])
        print(f"fib({n}) -> {fib(n)}")
    else:
        print("Must be one int parameter")




