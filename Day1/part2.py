import re

f = open('input.txt', 'r')
lines = f.readlines()

totalSum = 0

numberMap = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}


for l in lines:
    d1,d2=l,l[::-1]
    textNumber = re.findall('|'.join(numberMap), l)
    if textNumber:
        d1 = l.replace(textNumber[0], numberMap[textNumber[0]])
        
    textNumber = re.findall('|'.join(numberMap)[::-1], l[::-1])
    if textNumber:
        d2 = l.replace(textNumber[0][::-1], numberMap[textNumber[0][::-1]])[::-1]

    number1 = re.findall('[0-9]', d1) or [0]
    number2 = re.findall('[0-9]', d2) or [0]
    
    totalSum += int(str(number1[0]) + str(number2[0]))
    
print(totalSum)