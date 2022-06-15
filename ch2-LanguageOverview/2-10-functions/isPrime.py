
def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def primes():
    for i in range(100):
        if isPrime(i):
            print(i, end=" ", flush=True)
    print()


primes()


n = 4

isPrime(n)

if (isPrime(n)):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
