def main():
    grid = []
    with open('AdventOfCode/Day 4/input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            grid.append(line)

    xmasCount = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "X": continue
            
            # down, up, right, left, down-right diagonal, down-left diagonal, up-right diagonal, up-left diagonal
            for rowDir, colDir in [(1, 0), (-1, 0), (0, 1,), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                # check if we can even go 3 characters in the given direction
                if not (0 <= row + 3 * rowDir < len(grid) and 0 <= col + 3 * colDir < len(grid[0])): continue

                if grid[row + rowDir][col + colDir] == "M" and grid[row + 2 * rowDir][col + 2 * colDir] == "A" and grid[row + 3 * rowDir][col + 3 * colDir] == "S":
                    xmasCount += 1

    print(xmasCount)


main()