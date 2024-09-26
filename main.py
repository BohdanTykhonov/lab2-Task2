import math
from prime_checker import is_prime

def calculate_z(m):
    z = 1 / math.sqrt(m + math.sqrt(2))
    return z

if __name__ == "__main__":
    m = float(input("Введіть значення m: "))
    z = calculate_z(m)
    print(f"Значення z: {z}")

    n = int(input("Введіть число n для перевірки на простоту: "))
    if is_prime(n):
        print(f"Число {n} є простим.")
    else:
        print(f"Число {n} не є простим.")
