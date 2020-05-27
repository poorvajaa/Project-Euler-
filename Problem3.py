import math


def largest_prime_factor(num):
    max_prime = -1
    while num % 2 == 0:
        max_prime = 2
        num >> 1

    for count in range(3, int(math.sqrt(num)) + 1, 2):
        while num % count == 0:
            max_prime = count
            num = num / count

    if num > 2:
        max_prime = num

    return int(max_prime)


if __name__ == "__main__":
    number = 600851475143
    print(largest_prime_factor(number))
