from collections import defaultdict

def main():
    grid = getGrid()
    antennas = getAntennas(grid)
    answer = countAntinodes(antennas, grid)
    print(answer)                

# parses input file and returns a 2D array representing the grid
def getGrid():
    grid = []
    with open('Day 8/input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            grid.append(line)
    return grid

# returns a dictionary mapping antenna frequency to a list of all coordinates where an antenna of that freq appears
def getAntennas(grid):
    antennas = defaultdict(list) # frequency -> list of coords where every antenna of that frequency appears

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col != ".":
                antennas[col].append((i, j))
    return antennas

# returns true if the antinode coordinates are within the bounds of the grid
def checkBounds(antinode, grid):
    return 0 <= antinode[0] < len(grid) and 0 <= antinode[1] < len(grid[0])

def countAntinodes(antenna_list, grid):
    antinodes = set() # prevents me from counting duplicate antinodes

    for coord_list in antenna_list.values():
        if len(coord_list) == 1: continue # ignore frequencies with only one antenna
        for i in range(len(coord_list) - 1):
            pos1 = coord_list[i]
            for j in range(i + 1, len(coord_list)):
                pos2 = coord_list[j]
                row_diff = pos2[0] - pos1[0]
                col_diff = pos2[1] - pos1[1]

                antinodes.add(pos1)
                antinodes.add(pos2)

                # add all the antennas in line from pos1 if they are within the bounds of the grid
                antinode_pos = (pos1[0] - row_diff, pos1[1] - col_diff)
                while checkBounds(antinode_pos, grid):
                    antinodes.add(antinode_pos)
                    antinode_pos = (antinode_pos[0] - row_diff, antinode_pos[1] - col_diff)

                # do the same thing but from pos2 going the opposite direction
                antinode_pos = (pos2[0] + row_diff, pos2[1] + col_diff)
                while checkBounds(antinode_pos, grid):
                    antinodes.add(antinode_pos)
                    antinode_pos = (antinode_pos[0] + row_diff, antinode_pos[1] + col_diff)

    return len(antinodes)

main()

"""
Part 1 solution:

def main():
    grid = []
    with open('Day 8/input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            grid.append(line)
    
    print(grid)

    antinodes = set() # prevents me from counting duplicate antinodes

    # Finding every pair of antennas in the grid
    for first_row in range(len(grid)):
        for first_col in range(len(grid[0])):
            if grid[first_row][first_col] == ".": continue

            for second_row in range(first_row, len(grid)):
                for second_col in range(len(grid[0])):
                    if grid[second_row][second_col] == "." or (first_row == second_row and first_col == second_col): continue # don't compare an antenna with itself

                    if grid[first_row][first_col] == grid[second_row][second_col]:
                        row_diff = second_row - first_row
                        col_diff = second_col - first_col

                        # First antinode position
                        antinode1_row = first_row - row_diff
                        antinode1_col = first_col - col_diff

                        # Second antinode position
                        antinode2_row = second_row + row_diff
                        antinode2_col = second_col + col_diff

                        # Ensure positions are within bounds of grid and empty
                        if 0 <= antinode1_row < len(grid) and 0 <= antinode1_col < len(grid[0]):
                            antinodes.add((antinode1_row, antinode1_col))

                        if 0 <= antinode2_row < len(grid) and 0 <= antinode2_col < len(grid[0]):
                            antinodes.add((antinode2_row, antinode2_col))

    print(len(antinodes))

main()"""