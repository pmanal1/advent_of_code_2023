
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getLineNumber(line):
    start = -1
    end = -1

    index = 0
    while(start < 0):
        if(ord(line[index]) > 47 and ord(line[index]) < 58):
            start = int(line[index])
            break
        
        for number in numbers:
            lineSlice = line[index:index+len(number)]
            if(lineSlice.find(number) == 0):
                start = numbers.index(number) + 1
                break

        index += 1
    
    index = -1
    while(end < 0):
        if(ord(line[index]) > 47 and ord(line[index]) < 58):
            end = int(line[index])
            break
        
        for number in numbers:
            lineSlice = line[index-len(number):index]
            if(lineSlice.find(number) == 0):
                end = numbers.index(number) + 1
                break
        
        index -= 1
    
    return start * 10 + end

sum = 0
with open('input.txt') as file:
    for line in file:
        sum += getLineNumber(line)

    print(sum)
