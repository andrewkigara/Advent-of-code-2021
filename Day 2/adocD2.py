# Horizontal pos
# Vertical position

# Open file
# Readlines
# Split lines
# increase or decrease vert/horiz based on part 1 of line

def p1(file):
    horiz = 0
    vert = 0

    lines = open(file).readlines()

    for line in lines:
        line = line.split()
        if line[0] == 'forward':
            horiz += int(line[1])
        if line[0] == 'down':
            vert += int(line[1])
        if line[0] == 'up':
            vert -= int(line[1])
    print(horiz*vert)

def p2(file):
    horiz = 0
    vert = 0
    aim = 0

    lines = open(file).readlines()
    for line in lines:
        line = line.split()
        if line[0] == 'down':
            aim += int(line[1])
        if line[0] == 'up':
            aim -= int(line[1])
        if line[0] == 'forward':
            horiz += int(line[1])
            vert += aim*int(line[1])
    
    print(horiz*vert)

p1('adocD2.txt')
p2('adocD2.txt')