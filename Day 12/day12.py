# https://adventofcode.com/2024/day/12
from collections import deque

def main():
    grid = getGrid()
    regions = findRegions(grid)
    areas = findAreas(regions)
    sides = findSides(grid, regions)
    total_cost = calculateCost(areas, sides)
    print(total_cost)

def getGrid():
    with open('Day 12/input', 'r') as file:
        grid = file.read().splitlines()
    return grid

# Iterates through the entire grid calling bfs on distinct regions and keeping track of the regions in a list of sets
def findRegions(grid):
    regions = [] # will ultimately contain a list of sets for each region
    visited = set()
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) not in visited:
                region = bfs(grid, row, col, visited)
                regions.append(region)
    return regions

# bfs to find all coordinates that are part of a region
def bfs(grid, r, c, visited):
    queue = deque()
    region = set()
    crop = grid[r][c]
    visited.add((r, c))
    region.add((r, c))
    queue.append((r, c))

    while queue:
        cur_row, cur_col = queue.popleft()
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # cells can only connect a region if they are below, above, to the right or to the left of it. No diagonals
        
        for dr, dc in directions:
            new_row, new_col = cur_row + dr, cur_col + dc
            if (checkBounds((new_row, new_col), grid) and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == crop):
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                region.add((new_row, new_col))
    return region

def findAreas(regions):
    areas = []
    for region in regions:
        areas.append(len(region))
    return areas

def findSides(grid, regions):
    sides = []
    for region in regions:
        side_count = 0
        for row, col in region:
            # Check the diagonal cells and relevant adjacent cells
            for dr, dc, adj1, adj2 in [
                (-1, -1, (0, -1), (-1, 0)), # Top left 
                (-1, 1, (0, 1), (-1, 0)), # Top right 
                (1, -1, (0, -1), (1, 0)), # Bottom left 
                (1, 1, (0, 1), (1, 0)) # Bottom right 
            ]:
                diag_row, diag_col = row + dr, col + dc
                adj1_row, adj1_col = row + adj1[0], col + adj1[1]
                adj2_row, adj2_col = row + adj2[0], col + adj2[1]

                # Check if the diagonal and adjacent cells are out of bounds or part of a different region
                diag_outside = not checkBounds((diag_row, diag_col), grid) or (diag_row, diag_col) not in region
                adj1_outside = not checkBounds((adj1_row, adj1_col), grid) or (adj1_row, adj1_col) not in region
                adj2_outside = not checkBounds((adj2_row, adj2_col), grid) or (adj2_row, adj2_col) not in region

                # Count corner if the diagonal and its relevant adjacent cells are outside (outer corner)
                # Or if the diagonal is outside and both relevant cells are inside the region (inner corner)
                if diag_outside and (adj1_outside and adj2_outside):
                    side_count += 1
                if diag_outside and not (adj1_outside or adj2_outside):
                    side_count += 1
                if not diag_outside and (adj1_outside and adj2_outside): # this is a valid edge case for corners
                    side_count += 1

        sides.append(side_count)
    return sides

def calculateCost(areas, sides):
    total_cost = 0

    for i in range(len(areas)):
        cost = areas[i] * sides[i]
        total_cost += cost
    return total_cost

def checkBounds(coords, grid):
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])

main()


"""
Part 1 solution:

from collections import deque

def main():
    grid = getGrid()
    regions = findRegions(grid)
    areas = findAreas(regions)
    perimeters = findPerimeters(grid, regions)
    total_cost = calculateCost(areas, perimeters)
    print(total_cost)

def getGrid():
    with open('Day 12/input', 'r') as file:
        grid = file.read().splitlines()
    return grid

# Iterates through the entire grid calling bfs on distinct regions and keeping track of the regions in a list of sets
def findRegions(grid):
    regions = [] # will ultimately contain a list of sets for each region
    visited = set()
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) not in visited:
                region = bfs(grid, row, col, visited)
                regions.append(region)
    return regions

# bfs to find all coordinates that are part of a region
def bfs(grid, r, c, visited):
    queue = deque()
    region = set()
    crop = grid[r][c]
    visited.add((r, c))
    region.add((r, c))
    queue.append((r, c))

    while queue:
        cur_row, cur_col = queue.popleft()
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # cells can only connect a region if they are below, above, to the right or to the left of it. No diagonals
        
        for dr, dc in directions:
            new_row, new_col = cur_row + dr, cur_col + dc
            if (checkBounds((new_row, new_col), grid) and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == crop):
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                region.add((new_row, new_col))
    return region

def findAreas(regions):
    areas = []
    for region in regions:
        areas.append(len(region))
    return areas

def findPerimeters(grid, regions):
    perimeters = []

    for region in regions:
        perimeter = 0
        for row, col in region:
            # check neighbours in all directions, for each neighbour not in region, increment perimeter by 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor_row, neighbor_col = row + dr, col + dc

                if (not checkBounds((neighbor_row, neighbor_col), grid) or
                    (neighbor_row, neighbor_col) not in region):
                    perimeter += 1
        perimeters.append(perimeter)
    return perimeters

def calculateCost(areas, perimeters):
    total_cost = 0

    for i in range(len(areas)):
        cost = areas[i] * perimeters[i]
        total_cost += cost
    return total_cost

def checkBounds(coords, grid):
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])


main()"""