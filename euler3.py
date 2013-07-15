import sys
# Set prime factors found to zero
# This is where all found prime factors will be found
prime_factors = []
# Debug deepcount to stop endless recursion
deepcount = 0
startnum = 527981986973


def find_factors(num):
    global prime_factors
    global deepcount
    # All pre-checked factors
    factors = []
    # Set topwhile to num
    # This will be the upper end of the while loop
    topwhile = num

    #if deepcount > 20:
    #    sys.exit("Deepcount hit 20")

    #####
    # The loop
    #####
    # Init at 2, since all numbers will be factorable by 1
    i = 2
    # Find all the factors of num
    while i <= topwhile:
        if num % i == 0 and num != i:
            factors.append(i)
            topwhile = num / i
            print "Found factor of %d: %d." % (num, i)
            print "Reducing top limit to %d." % topwhile
        i += 1

    if len(factors) == 0:
        prime_factors.append(num)
        print "Found prime factor: %d." % num
    elif factors[0] < (num / 2):
        for j in range(0, len(factors)):
            print "Factorization complete of %d; factorize %d." % (num, factors[j])
            deepcount += 1
            find_factors(factors[j])
    else:
        print "Ending current recursion."

find_factors(startnum)


def sort_factors():
    global prime_factors
    prime_factors.sort()
    print "The largest prime factor of %d is %d." % (startnum, prime_factors[-1])

print "All prime factors: %r" % prime_factors
sort_factors()
