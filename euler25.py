# Finds the first factorial(n) that has 1000 digits.

strlen = 0
now = 1
last = 1
iterator = 2

while strlen < 1000:
    now += last
    last = now - last
    iterator += 1
    strlen = len(str(now))
    print "%d is %d long." % (iterator, strlen)
