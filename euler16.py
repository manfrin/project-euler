
num = 2**1000
strnum = str(num)
sum = 0
for x in range(0, len(strnum)):
    sum += int(strnum[x])
print sum
