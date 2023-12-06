colors = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def getColor(hand):
    for color in colors.keys():
        if(hand.find(color) != -1):
            return color

sum = 0
with open('input.txt') as file:
    for index, line in enumerate(file):
        line = line.split(": ")[1] # Removes Game x:
        hands = line.replace(";", ",").split(", ") # Splits each hand into its own index

        isGoodGame = True
        for hand in hands:
            if(int(hand[0:2]) > colors[getColor(hand)]): # If the number of cubes is greater than the expected number
                isGoodGame = False
        
        if(isGoodGame):
            sum += index + 1


print(sum)
        
