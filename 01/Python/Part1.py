from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open()
    return input.read()

def main():
    input = parseInput()
    level = 0
    for c in input:
        if c == "(": level += 1
        elif c == ")": level -= 1
        else:
            print("Error in input")
            exit(1)
    print(f'Santa should go to level: {level}')
    return

if __name__ == '__main__':
    main()