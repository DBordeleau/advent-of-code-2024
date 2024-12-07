def main():
    with open('Day 1\input', 'r') as file:
        nums1, nums2 = zip(*(line.split() for line in file))

    numCounts = {} # number -> frequency

    for num in nums2:
        if num not in numCounts:
            numCounts[num] = 1
        else:
            numCounts[num] += 1

    similarityScore = 0
    for num in nums1:
        if num in numCounts:
            similarityScore += int(num) * int(numCounts[num])
    
    print(similarityScore)

main()

"""
Part 1 solution:

def main():
    with open('input', 'r') as file:
        nums1, nums2 = zip(*(line.split() for line in file))
        
    nums1, nums2 = sorted(nums1), sorted(nums2)

    distance = 0
    for i in range(len(nums1)):
        distance += abs(int(nums1[i]) - int(nums2[i]))
    print(distance)

main()"""