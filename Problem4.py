def largest_palindrome(num):
    upper_lim = 0
    for i in range(1, num + 1):
        upper_lim = upper_lim * 10
        upper_lim = upper_lim + 9

    lower_lim = 1 + upper_lim // 10
    max_prod = 0
    for i in range(upper_lim, lower_lim - 1, -1):
        for j in range(i, lower_lim - 1, -1):
            prod = i * j
            if (prod < max_prod):
                break
            number = prod
            reverse = 0
            while (number != 0):
                reverse = reverse * 10 + number % 10
                number = number // 10

            if (prod == reverse and prod > max_prod):
                max_prod = prod
    return max_prod


if __name__ == "__main__":
    digit = 3
    print(largest_palindrome(digit))