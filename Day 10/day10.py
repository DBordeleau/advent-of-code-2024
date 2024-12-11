# https://adventofcode.com/2024/day/10
def main():
    grid = getGrid()

    total_ratings = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                total_ratings += walkAndCount(row, col, grid)
    print(total_ratings)

def getGrid():
    with open('Day 10/input', 'r') as file:
        grid = [list(map(int, line)) for line in file.read().splitlines()]
    return grid

# bfs that tries to traverse every valid path -- no need for adjacency representation from part 1
def walkAndCount(row, col, grid):
    height = grid[row][col]
    if height == 9: # base case: return 1 for the rating
        return 1
    
    rating = 0

    if col > 0 and grid[row][col - 1] == height + 1:
        rating += walkAndCount(row, col - 1, grid)
    if row > 0 and grid[row - 1][col] == height + 1:
        rating += walkAndCount(row - 1, col, grid)
    if col < len(grid[row]) - 1 and grid[row][col + 1] == height + 1:
        rating += walkAndCount(row, col + 1, grid)
    if row < len(grid[row]) - 1 and grid[row + 1][col] == height + 1:
        rating += walkAndCount(row + 1, col, grid)

    return rating

main()

"""
Part 1 solution:

def main():
    grid = getGrid()
    adjacency_dict, trailheads = buildAdjacencyList(grid)
    score = scoreTrails(adjacency_dict, trailheads, grid)
    print(score)

def getGrid():
    with open('Day 10/input', 'r') as file:
        grid = file.read().splitlines()
    return grid

# used by buildAdjacencyList to get a list of a given node's adjacent nodes
def getAdjacentNodes(row, col, grid):
    adjacent_coords = [(row, col-1), (row, col+1), (row - 1, col), (row + 1, col)]
    adjacency_list = []
    for coords in adjacent_coords:
        if checkBounds(coords, grid):
            adjacency_list.append(coords)
    return adjacency_list

# returns true if the node is within the bounds of the grid
def checkBounds(coords, grid):
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])

# builds and returns a dictionary mapping every node to all valid adjacent nodes and also returns a list of trailheads (nodes with height of 0)
def buildAdjacencyList(grid):
    trailheads = [] # list of all 0 height nodes
    adjacency_dict = {} # node -> adjacent nodes w/in grid bounds
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == "0":
                trailheads.append((row, col)) # keep track of trailheads
            node = (row, col)
            adjacent = getAdjacentNodes(row, col, grid)
            adjacency_dict[node] = adjacent
    return adjacency_dict, trailheads

# depth first search that looks for nodes with height of 9
def dfs(grid, trailhead, node, visited, reachable_peaks, adjacency_dict):
    row, col = node
    current_height = int(grid[row][col])

    # If the current node is height 9 add it to the set of reachable peaks
    if current_height == 9:
        reachable_peaks[trailhead].add(node)
        return

    visited.add(node)

    for neighbor in adjacency_dict[node]:
        neighbor_row, neighbor_col = neighbor
        neighbor_height = int(grid[neighbor_row][neighbor_col])

        # Continue DFS if the neighbor is 1 height greater than current node and not visited
        if neighbor not in visited and neighbor_height == current_height + 1:
            dfs(grid, trailhead, neighbor, visited, reachable_peaks, adjacency_dict)

# calls dfs on each trailhead and keeps track of the peaks that each trailhead can reach
# score is calculated as the sum of the unique # of peaks each trailhead can reach
def scoreTrails(adjacency_dict, trailheads, grid):
    reachable_peaks = {}
    for trailhead in trailheads:
        visited = set()
        reachable_peaks[trailhead] = set()
        dfs(grid, trailhead, trailhead, visited, reachable_peaks, adjacency_dict)

    score = 0
    # Sums the length of reachable peak sets for each node and returns the sum
    for trailhead in reachable_peaks:
        score += len(reachable_peaks[trailhead])
    return score

main()"""