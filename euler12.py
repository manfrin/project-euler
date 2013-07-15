

def divisors(n):
    # factors_of_n = []
    total_factors = 0
    for i in xrange(1, int(n ** .5)):
        if not n % i:
            total_factors += 2  # 2 for the divisor pair.
            # stra = '.' * total_factors
            # print "Found factor: %d %r" % (i, stra)
    #         factors_of_n.append(i)
    # factors_of_n.append(n)
    # f.write("%d,%d\n" % (total_factors, n))
    # return factors_of_n
    return total_factors


def check_to(n):
    is_found = False
    i = 2
    current_tri_num = 1
    while not is_found:
        current_tri_num += i
        if divisors(current_tri_num) >= n:
            is_found = True
        i += 1
    return current_tri_num

# print divisors(76576500)
# print "The first triangle number with at least 500 divisors is %d." % check_to(500)
# print divisors(1000)
# print divisors(339302)
# print check_to(10)
# f = open('euler12_r.csv', 'w')
# f.write("factors, number\n")
print(check_to(500))
# f.close()
