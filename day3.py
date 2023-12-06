# Read each line, iterate until you find a symbol done
# Once you find a symbol, check all around it to find any number
# Each number you find, reveal the whole number
# Return the numbers (removing duplicates along the way)

def isSymbol(char):
    if(ord(char) >= 21 and ord(char) <= 47 and ord(char) != 46):
        return True
    elif(ord(char) >= 58 and ord(char) <= 64):
        return True
    elif(ord(char) >= 91 and ord(char) <= 96):
        return True
    elif(ord(char) >= 123 and ord(char) <= 126):
        return True

# line - the entire line
# range - the proximity section of the line

# for each proximity section, check each index for a number
# if there is a number, go left and right until you get the whole number
# store it and delete duplicates
def getNumbers(line, range):
    numbers = []
    for index in range:
        if(line[index].isdigit()):
            start = index
            end = index

            while(line[start].isdigit() and start >= 0):
                start -= 1
            while(line[end].isdigit() and end <= len(line)):
                end += 1

            start += 1 # dumb bugs
            end -= 1

            number = int(line[start:end+1])

            if(number not in numbers):
                numbers.append(number)
    return numbers


partNumbers = []
sumGearRatio = 0
file = open('input.txt').readlines()

for lineIndex, line in enumerate(file):
    for charIndex, character in enumerate(line):
        if(isSymbol(character)):
            currentSymbolParts = []

            # Checking around the symbol for numbers (promixity sections)
            currentSymbolParts.extend(getNumbers(file[lineIndex - 1], range(charIndex - 1, charIndex + 2))) # The three above the symbol

            # One on each side of the symbol
            currentSymbolParts.extend(getNumbers(file[lineIndex], range(charIndex - 1, charIndex)))
            currentSymbolParts.extend(getNumbers(file[lineIndex], range(charIndex + 1, charIndex + 2)))

            currentSymbolParts.extend(getNumbers(file[lineIndex + 1], range(charIndex - 1, charIndex + 2))) # The three below the symbol

            partNumbers.extend(currentSymbolParts)
            if(len(currentSymbolParts) == 2 and character == "*"):
                sumGearRatio += currentSymbolParts[0] * currentSymbolParts[1]
            currentSymbolParts = []
            

sum = 0
for part in partNumbers:
    sum += part
print(sum)
print(sumGearRatio)