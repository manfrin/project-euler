topval = 998001
botval = 10000

palins = []
numsa = []
numsb = []

palinsin = []
lastpalin = 0


def fill_nums():
    global nums
    for i in range(100, 1000):
        numsa.append(i)


def find_palin():
    global palins
    holder = 0
    for i in range(botval, topval):
        holder = str(i)
        revholder = holder[::-1]
        if holder == revholder:
            palins.append(i)

find_palin()
fill_nums()
numsb = numsa[:]

# Cool, we've got all our ingredients, lets find these products.


def check_in():
    global lastpalin
    for i in numsa:
        for j in numsb:
            mult = i * j
            print "Multiplying %d by %d: %d " % (i, j, mult),
            print "Last palindrome: %d" % lastpalin
            if mult in palins:
                print "Palindrome!"
                lastpalin = mult
                palinsin.append(mult)

check_in()
print "Largest palindromic product: ", sorted(palinsin)[-1]
