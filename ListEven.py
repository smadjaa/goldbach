import sys

def isPrime(prime, primes):
    i = 0
    while i < len(primes):
        if prime % primes[i] == 0:
            return False
        i += 1
    return True

primes = [2, 3]
count = 4
i = 0
for i in range(0, int(sys.argv[1])):
    while not isPrime(count, primes):
        count += 1
    primes.append(count)
    i += 1
primes.sort()
list = {}
n = len(primes)
for i in range(0, n):
    for j in range(0, n):
        if (primes[i] + primes[j]) % 2 == 0:
            list[primes[i] + primes[j]] = "%d + %d" % (primes[i], primes[j])

f = open("goldbach.txt", "w")
for i in range(4, len(list)):
    if i % 2 == 0:
        f.write(" [%d = %s] " % (i, list[i]))
f.close()
