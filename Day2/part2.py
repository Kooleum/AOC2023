import re

f = open('input.txt', 'r')
lines = f.readlines()


def setPower(l):
    gameId = int(l.split(':', 1)[0][5:])
    
    l = re.sub('Game \d*:', '', l)
    
    sets = l.split(';')
    maxPerColor = {
        'red': 1,
        'green': 1,
        'blue': 1
    }
    
    for s in sets:
        for pick in s.split(', '):
            number = int(re.findall('\d+', pick)[0])
            color = re.findall('|'.join(maxPerColor), pick)[0]
            if number > maxPerColor[color]:
                maxPerColor[color] = number
                
    return maxPerColor['red'] * maxPerColor['green'] * maxPerColor['blue']


sumPower = 0

for l in lines:
    l = l.replace('\n', '')
    
    if len(l) < 5:
        continue
    
    sumPower += setPower(l)
    
print(sumPower)