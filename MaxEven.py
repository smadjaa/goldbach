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
i = j = -1
prime = primes[i] + primes[j]
while prime % 2 != 0:
    if i <= j:
        j -= 1
        prime = primes[i] + primes[j]
    else:
        i -= 1
        prime = primes[i] + primes[j]
print "%d = %d + %d" % (prime, primes[-1], primes[-1])