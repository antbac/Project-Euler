'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

single_digit = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

tens_digit = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '2X': 'twenty',
    '3X': 'thirty',
    '4X': 'forty',
    '5X': 'fifty',
    '6X': 'sixty',
    '7X': 'seventy',
    '8X': 'eighty',
    '9X': 'ninety'
}

def toString(number):
    if 0 >= number or number > 1000:
        raise Exception('This method can only handle numbers 1 through 1000')

    if 1 <= number and number <= 9:
        return single_digit[str(number)]

    string = ''
    
    if 1000 == number:
        return 'onethousand'

    if 100 <= number:
        string += single_digit[str(number)[-3]] + 'hundred'

        if str(number)[-2:] != '00':
            string += 'and'
    
    if int(str(number)[-2:]) >= 10 and int(str(number)[-2:]) < 20:
        return string + tens_digit[str(number)[-2:]]
    elif str(number)[-2] != '0':
        string += tens_digit[str(number)[-2] + 'X']

    return string + single_digit[str(number)[-1]]

total_length = 0
for i in range(1, 1001):
    total_length += len(toString(i))

print(total_length)