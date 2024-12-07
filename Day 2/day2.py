def main():
    safeCount = 0
    with open('Day 2\input', 'r') as file:
        reports = [ line.split() for line in file ]

    for report in reports:
        i = 0
        safe = True
        safety = True
        
        while i < len(report) - 1:
            if i == 0: # check if increasing/decreasing
                if int(report[i]) == int(report[i + 1]): # if the two adj levels are the same, the report is unsafe
                    if safety:
                        del report[i + 1]
                        safety = False
                        continue
                    safe = False
                    break

            increasing = int(report[0]) < int(report[1])

            adjDiff = abs(int(report[i]) - int(report[i + 1]))
            
            if (adjDiff > 3 or adjDiff < 1): # if increase/decrease by more than 3, or the numbers are the same the report is unsafe
                if safety:
                    del report[i + 1]
                    safety = False
                    continue
                safe = False
                break
            
            if (increasing) and (int(report[i]) > int(report[i + 1])):
                if safety:
                    del report[i + 1]
                    safety = False
                    continue
                safe = False
                break
            
            if not (increasing) and (int(report[i]) < int(report[i + 1])):
                if safety:
                    del report[i + 1]
                    safety = False
                    continue
                safe = False
                break

            i += 1

        if safe:
            safeCount += 1

    print(safeCount)
main()