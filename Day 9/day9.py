def main():
    with open('Day 9/input', 'r') as file:
        disk_map = file.read()
        disk_map = disk_map.rstrip('\n')
    
    file_blocks, free_blocks = getBlockLists(disk_map)
    blocks = createBlocks(file_blocks, free_blocks)
    blocks = compressFiles(blocks)
    print(blocks)
    #result = checkSum(blocks)
    #print(result)

# Splits the disk map into 2 int lists representing the file blocks and the free space blocks
def getBlockLists(disk_map):
    free_blocks = []
    file_blocks = []

    for i in range(len(disk_map)):
        if i % 2 == 0: # even indices are file blocks and odd are free blocks
            file_blocks.append(int(disk_map[i]))
        else:
            free_blocks.append(int(disk_map[i]))
    
    return file_blocks, free_blocks

# Returns a single list representing the block representation of the original puzzle input
def createBlocks(file_blocks, free_blocks):
    block_list = []
    for i in range(len(file_blocks)):
        block_list.append(str(i) * file_blocks[i])
        if i < len(free_blocks):  # free_blocks list has 1 less element than file_blocks
            block_list.append(["."] * free_blocks[i])
    return block_list

# Moves file blocks into valid memory blocks and returns the compressed list
def compressFiles(block_list):
    i = 0
    j = len(block_list) - 1
    while j >= 0:
        if "." not in block_list[j]: # if j is a file
            while j > i:
                # if the memory block is at least as long as the file move the file into the memory block
                if all(char == "." for char in block_list[i]) and (len(block_list[i]) >= len(block_list[j])):
                    file_len = len(block_list[j])
                    memory_len = len(block_list[i])

                    # move file into memory block index
                    block_list[i] = block_list[j]
                    
                    # calculate how many "." remain in memory block, if any
                    remaining_mem = memory_len - file_len
                    if remaining_mem > 0:
                        # add the remaining memory back into the list after the file
                        for _ in range(remaining_mem):
                            block_list.insert(i + 1, ".")
                    # replace file indices with moved memory space
                    del block_list[j]
                    for _ in range(file_len):
                        block_list.insert(j, ".")
                    break
                i += 1
        j -= 1
    return block_list

# Multiplies file ID by its index and returns the sum of these values for all file blocks
def checkSum(block_list):
    result = 0
    for i, block in enumerate(block_list):
        if "." not in block:
            result += i * int(block)
    return result

main()




"""
Part 1 solution:

def main():
    with open('Day 9/input', 'r') as file:
        disk_map = file.read()
        disk_map = disk_map.rstrip('\n')
    
    file_blocks, free_blocks = getBlockLists(disk_map)
    blocks = createBlocks(file_blocks, free_blocks)
    blocks = compressFiles(blocks)
    result = checkSum(blocks)
    print(result)

# Splits the disk map into 2 int lists representing the file blocks and the free space blocks
def getBlockLists(disk_map):
    free_blocks = []
    file_blocks = []

    for i in range(len(disk_map)):
        if i % 2 == 0: # even indices are file blocks and odd are free blocks
            file_blocks.append(int(disk_map[i]))
        else:
            free_blocks.append(int(disk_map[i]))
    
    return file_blocks, free_blocks

# Returns a single list representing the block representation of the original puzzle input
def createBlocks(file_blocks, free_blocks):
    block_list = []
    for i in range(len(file_blocks)):
        block_list.extend([str(i)] * file_blocks[i])
        if i < len(free_blocks):  # free_blocks list has 1 less element than file_blocks
            block_list.extend(["."] * free_blocks[i])
    return block_list

# Swaps file blocks from the end of the list to the first available free space
def compressFiles(block_list):
    i = 0
    j = len(block_list) - 1
    while i < j:
        if block_list[i] == ".":
            while j > i:
                if block_list[j] != ".":
                    block_list[i], block_list[j] = block_list[j], block_list[i]
                    break
                else:
                    j -= 1
        i += 1
    return block_list

# Multiplies file ID by its index and returns the sum of these values for all file blocks
def checkSum(block_list):
    result = 0
    for i, block in enumerate(block_list):
        if block != ".":
            result += i * int(block)
    return result

main()"""