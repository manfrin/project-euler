# Set up the checknumbers
# Omit: 1 because it'll always evaluate true
# Omit: 2, 3, 4, 5, 6, 7, 8, 9 because they are necessarily true for multiples
# Omit: 20 because we'll be checking multiples of 20
divisors = [19, 18, 17, 16, 15, 14, 13, 12, 11]

found = False
i = 1
while not found:
    num = i * 20
    print num
    allfound = True
    for j in divisors:
        if num % j != 0:
            allfound = False
    if allfound:
        found = True
    i += 1

print (i - 1) * 20
