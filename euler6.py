initial = 100
nums = []
for i in range(1, initial + 1):
    nums.append(i)


def addup(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return n + addup(n - 1)


def square_of_sums(n):
    x = addup(100)
    return pow(x, 2)


def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return pow(n, 2) + sum_of_squares(n - 1)

difference = square_of_sums(initial) - sum_of_squares(100)

print difference
