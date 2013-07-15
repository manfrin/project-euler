# Finding all primes under 2 million

def is_prime(n):
    for i in range(3, int(n ** .5) + 1, 2):
        if not n % i:
            return False
    return True


def prime_list(under):
    primes = [2, 3, 5, 7, 11, 13]
    i = max(primes) + 2
    while i < under:
        if is_prime(i):
            print "Adding prime %d" % i
            primes.append(i)
        i += 2
    return primes

print sum(prime_list(2000000))
