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

    nextNum = nums[0]
    numsRemaining = nums[1:]

    # Get the result for the concatenation operand (||) which combines digits from its left and right inputs
    # Example: 15 || 155 = 15155
    concatenatedNumber = int(str(current) + str(nextNum)) if current != 0 else nextNum # don't concatenate 0 on the first iteration

    # Try addition, multiplication and concatenation at every step of each recursive case
    # Returns true if any permutation of operands = the target
    return (checkOperands(target, numsRemaining, current + nextNum) or
            checkOperands(target, numsRemaining, current * nextNum if current != 0 else nextNum) or # when current is 0, start multiplication with next num, otherwise it's always going to be 0
            checkOperands(target, numsRemaining, concatenatedNumber))

main()