def multiples_3_and_5():
    sum = 0
    for value in range(0, 1000):
        if value % 3 == 0 or value % 5 == 0:
            sum += value
    return sum


print(multiples_3_and_5())
