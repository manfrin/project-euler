

# Steps are an index value, so start at one or increment returned value
def step(at, steps):
    # print "%d on hop %d" % (at, steps)
    while not at == 1:
        if at % 2 == 0:
            at, steps = step(at / 2, steps + 1)
        else:
            at, steps = step(((at * 3) + 1), steps + 1)
        break
    return (1, steps)

maxhops = {'at': 0, 'steps': 0}

for i in range(1, 1000001):
    at, steps = step(i, 1)
    if steps > maxhops['steps']:
        maxhops['steps'] = steps
        maxhops['at'] = at
        print "Max found: %d (%d steps at %d)" % (i, steps, at)
