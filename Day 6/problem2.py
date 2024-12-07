guardPath = []
def main():
    guardMap = []
    results = []

    with open('AdventOfCode/Day 6/input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            guardMap.append(list(line))
    
    guardRow, guardCol = findGuard(guardMap)
    # Sim initial guard path
    moveGuard(guardMap, guardRow, guardCol, False)

   
    for coords in guardPath:
        row, col = coords
        # Place obstacle and check for cycle
        original = guardMap[row][col]  
        guardMap[row][col] = "#"
        if moveGuard(guardMap, guardRow, guardCol, True):
            results.append((row, col))
        guardMap[row][col] = original  # Restore map after every check

    print(len(results))

def findGuard(guardMap):
    directions = ["^", ">", "v", "<"]
    for row in range(len(guardMap)):
        for col in range(len(guardMap[0])):
            if guardMap[row][col] in directions:
                return row, col

def moveGuard(guardMap, startRow, startCol, cycleCheck):
    visited = set()
    row, col = startRow, startCol
    direction = "^"

    while True:
        # If we visited the same position going the same direction, we have a cycle
        if cycleCheck:
            if (row, col, direction) in visited:
                return True
            visited.add((row, col, direction))

        if guardMap[row][col] == ".":
            guardMap[row][col] = "X" 
            if not cycleCheck:
                guardPath.append((row, col))

        if direction == "^":
            row -= 1
        elif direction == ">":
            col += 1
        elif direction == "v":
            row += 1
        elif direction == "<":
            col -= 1

        # Check if the guard exits map or hits an obstacle
        if row < 0 or row >= len(guardMap) or col < 0 or col >= len(guardMap[0]):
            if cycleCheck:
                return False
            return
        if guardMap[row][col] == "#":
            if direction == "^":
                row += 1
            elif direction == ">":
                col -= 1
            elif direction == "v":
                row -= 1
            else:
                col += 1
            direction = turnRight(direction)

def turnRight(direction):
    # turn right when we hit an obstacle
    directions = ["^", ">", "v", "<"]
    return directions[(directions.index(direction) + 1) % 4]

main()