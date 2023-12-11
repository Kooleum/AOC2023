import math

f = open('input.txt', 'r')
lines = f.readlines()

totalPoints = 0

nbPerCards = [1] * len(lines)

for (i, l) in enumerate(lines):
    if len(l) < 5:
        continue
    
    
    l = l.split(':')[1]
    numbers = l.split('|')
    winningNumbers = numbers[0].strip().replace('  ', ' ').split(' ')
    myNumbers = numbers[1].strip().replace('  ', ' ').split(' ')
    
    nbWinning = len(set(winningNumbers) & set(myNumbers))
    for j in range(nbWinning):
        nbPerCards[i + j + 1] += 1 * nbPerCards[i]

print(sum(nbPerCards))