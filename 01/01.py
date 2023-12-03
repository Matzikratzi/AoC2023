#!/bin/python

def calibVal(line):
    res = [int(i) for i in [*line] if i.isdigit()]
    return(10 * int(res[0]) + int(res[-1]))

def translateNumStr(string):
    numbers = ['zero', 0,
               '0', 0,
               'one', 1,
               '1', 1,
               'two', 2,
               '2', 2,
               'three', 3,
               '3', 3,
               'four', 4,
               '4', 4,
               'five', 5,
               '5', 5,
               'six', 6,
               '6', 6,
               'seven', 7,
               '7', 7,
               'eight', 8,
               '8', 8,
               'nine', 9,
               '9', 9]

    i = 0
    while i < len(numbers):
        if string == numbers[i]:
            return(numbers[i+1])
        i += 1

def calibVal2(line):
    i = 0
    res = []
    nums =  ['zero',
               '0',
               'one',
               '1',
               'two',
               '2',
               'three',
               '3',
               'four',
               '4',
               'five',
               '5',
               'six',
               '6',
               'seven',
               '7',
               'eight',
               '8',
               'nine',
               '9']
    while i < len(line):
        lin = line[i:len(line)]
        for n in nums:
            if lin[:len(n)] == n:
                res.append(translateNumStr(n))
        i += 1

    return(10 * int(res[0]) + int(res[-1]))
    
filename='input.txt'

summa = 0

with open(filename) as f:
   for line in f:
       val = calibVal(line)
       summa += val

print(summa)

summa = 0

with open(filename) as f:
    summa = 0
    for line in f:
       val = calibVal2(line)
#       print(str(val))
       summa += val

print(summa)
