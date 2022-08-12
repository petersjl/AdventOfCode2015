from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open()
    return input.read()

def main():
    input = parseInput()
    level = 0
    found = False
    firstBasement = 0
    for i in range(len(input)):
        c = input[i]
        if c == "(": level += 1
        elif c == ")": level -= 1
        else:
            print("Error in input")
            exit(1)
        if not found and level == -1:
            found = True
            firstBasement = i + 1
    print(f'Santa should go to level: {level}\nHe first reached the basement at position: {firstBasement}')
    return

if __name__ == '__main__':
    main()