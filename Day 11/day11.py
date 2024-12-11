from collections import defaultdict

def main():
    stones = defaultdict(int)
    split_stones = {} # stores the left and right half of a split stone as an ordered pair

    with open('Day 11/input', 'r') as file:
        for stone in map(int, file.read().rstrip("\n").split()):
            stones[stone] += 1
    
    for _ in range(75):
        stones = blink(stones, split_stones)
    print(sum(stones.values()))

def blink(stones, split_stones):
    new_stones = defaultdict(int) # number -> freq

    if 0 in stones:
        new_stones[1] += stones[0] # Every 0 stone in the old set becomes a 1 stone when we blink
        del stones[0]

    for stone, count in stones.items():
        if stone in split_stones: # if there were stones that got split last blink, update their counts
            new_stones[split_stones[stone][0]] += count 
            new_stones[split_stones[stone][1]] += count
        elif len(str(stone)) % 2 == 0: # split stones on this blink
            mid = len(str(stone)) // 2
            left_digits = int(str(stone)[:mid])
            right_digits = int(str(stone)[mid:])
            new_stones[left_digits] += count
            new_stones[right_digits] += count
            split_stones[stone] = (left_digits, right_digits)
        else:
            new_stones[stone * 2024] += count
    return new_stones

main()

"""
Part 1 solution:

def main():
    with open('Day 11/input', 'r') as file:
        stones = file.read().rstrip("\n")
    stones = list(stones.split(" "))
    
    for _ in range(75):
        stones = blink(stones)
    print(len(stones))

def blink(stones: list, blinks):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left_digits = stone[:mid]
            right_digits = str(int(stone[mid:])) # int conversion removes leading zeros
            new_stones.append(left_digits)
            new_stones.append(right_digits)
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones

main()"""