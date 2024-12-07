def main():
    with open('input', 'r') as file:
        nums1, nums2 = zip(*(line.split() for line in file))
        
    nums1, nums2 = sorted(nums1), sorted(nums2)

    distance = 0
    for i in range(len(nums1)):
        distance += abs(int(nums1[i]) - int(nums2[i]))
    print(distance)

main()