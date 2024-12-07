def main():
    pageMap = {} # page -> list of pages that must come before it
    updateList = []
    badUpdates = []
    answer = 0
    with open("Day 5\input", "r") as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                num1, num2 = line.split('|')
                num1, num2 = int(num1), int(num2)
                if num2 not in pageMap:
                    pageMap[num2] = [num1]
                else:
                    pageMap[num2].append(num1)
            elif line and '|' not in line:
                update = list(line.split(','))
                update = [int(num) for num in update]
                updateList.append(update)

    for update in updateList:
        for i, num in enumerate(update):
            if num in pageMap:
                requiredPages = pageMap[num]
                # if any page from the dict appears after the current element in the list, the update is invalid
                if any(page in update[i+1:] for page in requiredPages):
                    badUpdates.append(update)
                    break

    for update in badUpdates:
        i = 0
        while i < len(update):
            j = len(update) - 1
            while i < j:
                if update[i] in pageMap:
                    if update[j] in pageMap[update[i]]:
                        update[i], update[j] = update[j], update[i]
                        j = len(update) - 1
                    else: 
                        j -= 1
                else: break
            i += 1
        mid = update[len(update) // 2]
        answer += mid

    print(answer)

main()

"""
Part 1 solution

def main():
    pageMap = {} # page -> list of pages that must come before it
    updateList = []
    answer = 0
    with open("AdventOfCode\Day 5\input", "r") as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                num1, num2 = line.split('|')
                num1, num2 = int(num1), int(num2)
                if num2 not in pageMap:
                    pageMap[num2] = [num1]
                else:
                    pageMap[num2].append(num1)
            elif line and '|' not in line:
                update = list(line.split(','))
                update = [int(num) for num in update]
                updateList.append(update)

    for update in updateList:
        valid = True
        for i, num in enumerate(update):
            if num in pageMap:
                requiredPages = pageMap[num]
                # if any page from the dict appears after the current element in the list, the update is invalid
                if any(page in update[i+1:] for page in requiredPages):
                    valid = False
                    break
        if valid:
            mid = update[len(update) // 2]
            answer += mid

    print(answer)

main()"""