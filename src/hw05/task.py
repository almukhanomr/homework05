import random

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> list[int]:
    prime_list = []
    num = 2
    while len(prime_list) < count:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

def checksum(numbers: list[int]) -> int:
    result = 0
    for num in numbers:
        result = (result + num) * 113
    result %= 10_000_007
    return result


def pipeline() -> int:
    prime_numbers = primes(1000)

    random.seed(100)
    random.shuffle(prime_numbers)

    return checksum(prime_numbers)