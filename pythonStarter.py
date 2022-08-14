from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open().read()
    return input

def main():
    input = parseInput()
    return

if __name__ == '__main__':
    main()