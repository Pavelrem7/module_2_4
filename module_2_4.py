numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
for k in numbers:
    is_prime = True
    if k == 1:
        continue
    else:
        for j in range(2, k - 1):
            if k % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(k)
    else:
        not_primes.append(k)

print('primes:', primes)
print('not_primes:', not_primes)