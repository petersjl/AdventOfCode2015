from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open().read()
    return input.split("\n")

def main():
    input = parseInput()
    niceStrings = []
    for string in input:
        if checkNice(string): niceStrings.append(string)
    print(f'There are {len(niceStrings)} nice strings')
    return

def checkNice(string: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u']
    disallowed = ['ab', 'cd', 'pq', 'xy']
    vowelCount = 0
    double = False
    if vowels.count(string[0]) != 0: vowelCount += 1
    for i in range(1, len(string)):
        a = string[i-1]
        b = string[i]
        if a == b: double = True
        if disallowed.count(a + b) != 0: return False
        if vowels.count(b) != 0: vowelCount += 1        
    return vowelCount > 2 and double

if __name__ == '__main__':
    main()