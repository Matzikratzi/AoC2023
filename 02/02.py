#!/bin/python

filename = 'input.txt'

maxReds   = 12
maxGreens = 13
maxBlues  = 14

def minFinder(line):
    reds   = 0
    blues  = 0
    greens = 0
    
    [game, setsString] = line.split(':')
    [txt, gameNum] = game.split()
    sets = setsString.split(';')
    
    # print(gameNum)
    for s in sets:
        pairs = s.split(',')
        # print(pairs)
        for p in pairs:
            ps = p.strip()
            # print(ps)
            [n, c] = ps.split()
            # print(c)
            if c == 'red':
                if int(n) > reds:
                    reds = int(n)
            if c == 'green':
                if int(n) > greens:
                    greens = int(n)
            if c == 'blue':
                if int(n) > blues:
                    blues = int(n)
    # print(gameNum + ' ' + str(stat))
    return reds * blues * greens

def randChecker(line):
    stat = True
    [game, setsString] = line.split(':')
    [txt, gameNum] = game.split()
    sets = setsString.split(';')
    
    # print(gameNum)
    for s in sets:
        pairs = s.split(',')
        # print(pairs)
        for p in pairs:
            ps = p.strip()
            # print(ps)
            [n, c] = ps.split()
            # print(c)
            if c == 'red':
                if int(n) > maxReds:
                    stat = False
            if c == 'green':
                if int(n) > maxGreens:
                    stat = False
            if c == 'blue':
                if int(n) > maxBlues:
                    stat = False
    # print(gameNum + ' ' + str(stat))
    if stat == True:
        return int(gameNum)
    else:
        return 0

summa = 0
    
with open(filename) as f:
   for line in f:
       num = randChecker(line)
       summa += num

print(summa)

summa = 0

with open(filename) as f:
   for line in f:
       power = minFinder(line)
       summa += power

print(summa)
