# Day 4 Part 2
# start with card 1, count the number of matches
# the number of matches corresponds to the number of copies of the next n cards
# make a queue "array" corresponding to the copies of the next n cards
# add one to the total amount of cards
# pop the first index of the queue
# on the next iteration, perform step 1 queue[0] + 1 times
# add queue[0] + 1 to the total amount of cards

# instead of performing step 1 queue[0] + 1 times, add queue[0] + 1 when adding the copies of cards

# removes empty spaces in list
def filterList(x):
    for index, element in enumerate(x):
        x[index] = element.strip()
    return list(filter(lambda x: (x != ""), x))

file = open('input.txt').readlines()

numCards = 0
queue = [0]
for lineIndex, line in enumerate(file):
    line = line.split(": ")[1] # Remove Game X:
    
    winningNumbers = line.split(" | ")[0].split(" ")
    myNumbers = line.split(" | ")[1].split(" ")

    winningNumbers = filterList(winningNumbers)
    myNumbers = filterList(myNumbers)

    if(len(queue) == 0): # just in case the queue is empty, the for loop needs to continue
        queue.append(0)
    
    copiesToMake = 0
    for myNumber in myNumbers:
        if(myNumber in winningNumbers):
            copiesToMake += 1
    
    index = 1
    while(copiesToMake > 0): # Go through the queue and add the copies
        if(len(queue) - 1 < index): # indicates the first copy of a game, need to append
            queue.append(queue[0] + 1) 
        else:
            queue[index] += queue[0] + 1 # queue[0] + 1 because that's how many copies of the current card we have
        
        copiesToMake -= 1
        index += 1
    
    numCards += queue.pop(0) + 1
            
print(numCards)
