# Each line is a card, the set of numbers to the left are the winning numbers, the set of numbers to the right are your numbers
# For each card:
#   Check how many matches there are
#   Count up the points (exponent 2)
#   Add it to a sum

# removes empty spaces in list
def filterList(x):
    for index, element in enumerate(x):
        x[index] = element.strip()
    return list(filter(lambda x: (x != ""), x))

file = open('input.txt').readlines()

totalPoints = 0
for lineIndex, line in enumerate(file):
    line = line.split(": ")[1] # Remove Game X:
    
    winningNumbers = line.split(" | ")[0].split(" ")
    myNumbers = line.split(" | ")[1].split(" ")

    winningNumbers = filterList(winningNumbers)
    myNumbers = filterList(myNumbers)

    print(winningNumbers)
    print(myNumbers)

    currentCardPoints = 0
    for myNumber in myNumbers:
        if(myNumber in winningNumbers):
            if(currentCardPoints == 0):
                print("start", myNumber)
                currentCardPoints += 1
            else:
                print("yay", myNumber)
                currentCardPoints *= 2
    
    print("total", currentCardPoints)
    totalPoints += currentCardPoints

print(totalPoints)