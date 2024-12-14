# https://adventofcode.com/2024/day/14
import re

def main():
    robot_list = getRobots()
    simRobots(robot_list, 10000)

def getRobots():
    robots = []

    # regex pattern to extract x and y values for position and velocity
    robot_pattern = r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)'

    with open('Day 14/input', 'r') as file:
        input_lines = file.read().splitlines()
        for i in range(len(input_lines)):
            data = re.search(robot_pattern, input_lines[i])

            p_x, p_y, v_x, v_y = map(int, data.groups())
            position = (p_x, p_y)
            velocity = (v_x, v_y)

            robots.append([position, velocity])
        return robots

# simulates robot movement over X seconds and returns the list with updated robot positions
def simRobots(robot_list, seconds):
    # grid boundaries defined in problem
    num_rows = 103
    num_cols = 101

    with open('Day 14/output', 'w') as file:
        for second in range(seconds):
            grid = [["."] * num_cols for _ in range(num_rows)]
            for robot in robot_list:
                p_x, p_y, v_x, v_y = robot[0][0], robot[0][1], robot[1][0], robot[1][1]

                new_p_x = (p_x + v_x) % num_cols
                new_p_y = (p_y + v_y) % num_rows

                # handles negative modulo
                if new_p_x < 0:
                    new_p_x += num_cols
                if new_p_y < 0:
                    new_p_y += num_rows

                robot[0] = (new_p_x, new_p_y)
                grid[new_p_y][new_p_x] = "*"
            
            file.write(f"Second {second + 1}:\n")

            for row in grid:
                file.write("".join(row) + "\n")

            # Add a blank line between seconds for clarity
            file.write("\n")

    print(f"Output saved.")

main()


"""
Part 1 solution:

import re

def main():
    robot_list = getRobots()
    safety_factor = simRobots(robot_list, 100)
    print(safety_factor)

def getRobots():
    robots = []

    # regex pattern to extract x and y values for position and velocity
    robot_pattern = r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)'

    with open('Day 14/input', 'r') as file:
        input_lines = file.read().splitlines()
        for i in range(len(input_lines)):
            data = re.search(robot_pattern, input_lines[i])

            p_x, p_y, v_x, v_y = map(int, data.groups())
            position = (p_x, p_y)
            velocity = (v_x, v_y)

            robots.append([position, velocity])
        return robots

# simulates robot movement over X seconds and returns the list with updated robot positions
def simRobots(robot_list, seconds):
    # grid boundaries defined in problem
    num_rows = 103
    num_cols = 101

    for robot in robot_list:
        p_x, p_y, v_x, v_y = robot[0][0], robot[0][1], robot[1][0], robot[1][1]

        # new robot positions after X seconds
        new_p_x = (p_x + (v_x * seconds)) % num_cols
        new_p_y = (p_y + (v_y * seconds)) % num_rows

        # handles negative modulo
        if new_p_x < 0:
            new_p_x += num_cols
        if new_p_y < 0:
            new_p_y += num_rows

        robot[0] = (new_p_x, new_p_y)
    
    # count the robots based on their new positions
    return countRobots(robot_list, num_rows, num_cols)

def countRobots(robot_list, num_rows, num_cols):
    # top-left, top-right, bottom-left, bottom-right quadrants
    # tracking these separately instead of a running total in case quadrants are relevant for part 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for robot in robot_list:
            p_x, p_y = robot[0][0], robot[0][1]

            if p_x == num_cols // 2 or p_y == num_rows // 2:
                continue

            left = p_x < (num_cols // 2)
            right = p_x > (num_cols // 2) 
            top = p_y < (num_rows // 2) 
            bottom = p_y > (num_rows // 2)

            if left and top:
                q1 += 1
            if right and top:
                q2 += 1
            if left and bottom:
                q3 += 1
            if right and bottom:
                q4 += 1
    return (q1 * q2 * q3 * q4)

main()"""