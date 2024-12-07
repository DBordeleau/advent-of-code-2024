def main():
    targets = []
    numList = []
    result = 0
    with open('AdventOfCode\Day 7\input', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            target, nums = line.split(": ")
            nums = [int(num) for num in nums.split(" ")]
            targets.append(int(target))
            numList.append(nums)

    for i, target in enumerate(targets):
        if checkOperands(target, numList[i]):
            result += target
    
    print(result)

# Recursively adds and multiplies every num in numList from left to right (as per specs order of operations doesn't apply to this problem)
# Returns true if we can achieve the target
def checkOperands(target, nums, current = 0):
    # Base case: If we run out of numbers check if the current value = the target
    if not nums:
        return current == target

    next_num = nums[0]
    remaining_nums = nums[1:]

    # Try addition and multiplication and check next num
    return (checkOperands(target, remaining_nums, current + next_num) or
            checkOperands(target, remaining_nums, current * next_num if current != 0 else next_num)) # when current is 0, start multiplication with next num, otherwise it's always going to be 0

main()