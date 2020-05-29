import math


def smallest_divisible_number():
    val = 1
    for value in range(1, 21):
        val *= value // math.gcd(value, val)
    return str(val)


if __name__ == "__main__":
    print(smallest_divisible_number())
