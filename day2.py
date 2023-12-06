# For each game, count the highest cubes for each color
# Then, multiply the counts to make a power
# Sum it up

colors = {
    "red": 0,
    "green": 0,
    "blue": 0
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

        for hand in hands:
            # get the color
            # check the count of this hand compared to the max currently, replace if its greater

            if(int(hand[0:2]) > colors[getColor(hand)]):
                colors[getColor(hand)] = int(hand[0:2])

        power = colors["red"] * colors["green"] * colors["blue"]
        sum += power

        # Reset the max counts for the next game
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

print(sum)
        
