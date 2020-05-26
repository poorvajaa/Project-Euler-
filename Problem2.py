def fibonacci():
    total = 0
    curr_num = 1
    next_num = 2
    while curr_num <= 4000000:
        if curr_num % 2 == 0:
            total += curr_num
        curr_num, next_num = next_num, curr_num + next_num
    return str(total)

if __name__ == "__main__":
    print(fibonacci())