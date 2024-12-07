def main():
    guardMap = []
    answer = 0
    with open('AdventOfCode\Day 6\input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            guardMap.append(list(line))
    
    guardRow, guardCol = findGuard(guardMap)
    moveGuard(guardMap, guardRow, guardCol, "^")
    
    for row in guardMap:
        for col in row:
            if col == "X":
                answer += 1

    print(answer)

def findGuard(guardMap):
    directions = ["^", ">", "v", "<"]
    for row in range(len(guardMap)):
        for col in range(len(guardMap[0])):
            if guardMap[row][col] not in directions: continue
            moveGuard(guardMap, row, col, "^")
            return row, col
        
def moveGuard(guardMap, row, col, direction): 
    while True:
            if guardMap[row][col] == ".":
                guardMap[row][col] = "X" 

            if direction == "^":
                row -= 1
            elif direction == ">":
                col += 1
            elif direction == "v":
                row += 1
            elif direction == "<":
                col -= 1
            # check if guard exits map or hits an obstacle
            if row < 0 or row >= len(guardMap) or col < 0 or col >= len(guardMap[0]):
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