def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n == 1:
            return f"{n} - Не простое"
        else:
            if n % 2 ==0:
                return f"{n} - Составное"
            for div in range(3, int(n**0.5)+1, 2):
                if n % div == 0:
                    return f"{n} - Составное"
            return f"{n} - Простое"
    return wrapper
@is_prime
def sum_three(x, y, z):
    return x+y+z

print(sum_three(24000, 25000, 999))