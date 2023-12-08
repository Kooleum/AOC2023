import re

f = open('input.txt', 'r')
lines = f.readlines()

totalSum = 0

for l in lines:
    numbers = re.findall('[0-9]', l) or [0]
    totalSum += int(numbers[0]+numbers[-1])
    
print(totalSum)