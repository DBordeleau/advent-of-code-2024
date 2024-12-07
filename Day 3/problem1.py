import re

def main():
    with open('AdventOfCode/Day 3/input', 'r') as file:
        txt = file.read()

    if not txt.startswith("do()"):
        txt = "do()" + txt

    matches = re.findall(r"do\(\)(.*?)don't\(\)", txt, re.DOTALL)

    clean = re.compile(r"mul\((\d+),(\d+)\)")

    results = []
    for match in matches:
        multiplicationList = clean.findall(match)
        results.extend(int(a) * int(b) for a, b in multiplicationList)
    
    print(sum(results))

main()
