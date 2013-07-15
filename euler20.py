# Finds 100! factorial


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


longnum = factorial(100)
longstr = str(longnum)

total = 0

for each in longstr:
    total += int(each)

print total
