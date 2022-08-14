from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open().read()
    return input.split("\n")

def main():
    input = parseInput()
    niceStrings = 0
    for string in input:
        if checkNice(string): niceStrings += 1
    print(f'There are {niceStrings} nice strings')
    return

def checkNice(string: str) -> bool:
    vowelCount = 0
    double = False
    pair = False
    first = string[0] + string[1]
    pairs = [first]
    for i in range(2, len(string)):
        first = string[i - 2] + string[i - 1]
        second = string[i - 1] + string[i]
        if not pair:
            if first != second:
                if second in pairs: pair = True
                else: pairs.append(second)
        if string[i-2] == string[i]: double = True
        if double and pair: return True
            
    return False

if __name__ == '__main__':
    main()