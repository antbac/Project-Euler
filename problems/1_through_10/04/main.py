'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    largest = -1
    for a in range(100, 1000):
        for b in range(a, 1000):
            product = a * b
            if is_palindrome(product):
                largest = max(largest, product)
    print(largest)