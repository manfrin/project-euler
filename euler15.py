x = 0
y = 0
totalcount = 0


def nextstep(px, py):
    global totalcount
    if px >= 19 and py >= 19:
        totalcount += 1
        return 1
    elif px >= 19 and py < 19:
        return nextstep(px, py + 1)
    elif py >= 19 and px < 19:
        return nextstep(px + 1, py)
    else:
        nextstep(px + 1, py)
        print "XX+ %d, %d" % (px, py)
        nextstep(px, py + 1)
        print "-YY+ %d, %d" % (px, py)

nextstep(x, y)
print totalcount
