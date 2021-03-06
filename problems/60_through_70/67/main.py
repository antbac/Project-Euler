'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)
'''

numbers = []
with open('triangle.txt', 'r') as input_file:
    for line in input_file.readlines():
        numbers.append([int(x) for x in line.split(' ')])

for y in range(len(numbers) - 2, -1, -1):
    for x in range(0, len(numbers[y])):
        numbers[y][x] = numbers[y][x] + max(numbers[y+1][x], numbers[y+1][x+1])

print(numbers[0][0])