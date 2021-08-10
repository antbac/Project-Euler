'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def get_primes_up_to(max_number):
    sieve = [True] * max_number
    primes = []
    for i in range(2, max_number - 1):
        if sieve[i + 1]:
            for x in range(i, max_number - 1, i):
                sieve[x + 1] = False
            primes.append(i)
    return primes

if __name__ == '__main__':
    max_number = 2000000
    print(sum(get_primes_up_to(max_number)))