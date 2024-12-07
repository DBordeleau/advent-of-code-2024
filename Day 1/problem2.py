def main():
    with open('input', 'r') as file:
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