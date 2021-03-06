'''
The sum of the squares of the first ten natural numbers is:
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

if __name__ == '__main__':
    min_number = 1
    max_number = 100

    a = sum([i**2 for i in range(min_number, max_number + 1)])
    b = sum([i for i in range(min_number, max_number + 1)])**2

    print(b - a)