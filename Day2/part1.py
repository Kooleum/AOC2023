import re

f = open('input.txt', 'r')
lines = f.readlines()

MAX_COLOR = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def getGameIdIfPossible(l):
    gameId = int(l.split(':', 1)[0][5:])
    
    l = re.sub('Game \d*:', '', l)
    
    sets = l.split(';')
    for s in sets:
        for pick in s.split(', '):
            number = int(re.findall('\d+', pick)[0])
            color = re.findall('|'.join(MAX_COLOR), pick)[0]
            if number > MAX_COLOR[color]:
                return 0
            
    return gameId


gameIdsSum = 0

for l in lines:
    l = l.replace('\n', '')
    
    if len(l) < 5:
        continue
    
    gameIdsSum += getGameIdIfPossible(l)
    
print(gameIdsSum)