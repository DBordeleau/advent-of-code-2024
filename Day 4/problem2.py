def main():
    grid = []
    with open('AdventOfCode/Day 4/input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            grid.append(line)

    xmasCount = 0
    diagonalList = []
    goodDiagonals = ["MMSS", "SSMM", "MSSM", "SMMS"]

    for row in range(1, len(grid) - 1): # start at 1 instead of 0 because the A cannot be on the edge of the grid
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] != "A": continue
            
            diagonals = "".join([grid[row - 1][col - 1], grid[row - 1][col + 1], grid[row + 1][col + 1], grid[row + 1][col - 1]])
            diagonalList.append(diagonals)
    for diagonal in diagonalList:
        if diagonal in goodDiagonals:
            xmasCount += 1
    print(xmasCount)

main()