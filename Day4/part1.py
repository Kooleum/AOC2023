import math

f = open('input.txt', 'r')
lines = f.readlines()

totalPoints = 0

for l in lines:
    if len(l) < 5:
        continue
    
    nbWinning = 0
    
    l = l.split(':')[1]
    numbers = l.split('|')
    winningNumbers = numbers[0].strip().replace('  ', ' ').split(' ')
    myNumbers = numbers[1].strip().replace('  ', ' ').split(' ')
    
    totalPoints += math.trunc(pow(2,len(list(set(winningNumbers) & set(myNumbers)))-1))
    
print(totalPoints)