for a in range(1, 1000):
    for b in range(1, 1000):
        c2 = (a * a) + (b * b)
        c = c2 ** .5
        # print "A: %d, B: %d, C: %d" % (a, b, c)
        if a + b + c == 1000:
            print "a: %d b: %d c: %d" % (a, b, c)
            exit
