from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open()
    return input.read()

def main():
    input = parseInput()
    x = 0
    y = 0
    houses = {0: {0: 1}}
    for c in input:
        if c == "^": y += 1
        elif c == "v": y -= 1
        elif c == ">": x += 1
        elif c == "<": x -= 1
        else:
            print(f'Invalid input: {c}')
            exit()
        if houses.get(x):
            if houses[x].get(y): houses[x][y] += 1
            else: houses[x][y] = 1
        else: houses[x] = {y: 1}
    count = 0
    for dict in houses:
        count += len(houses[dict].keys())
    #print(houses)
    print(f'Houses with at least one present: {count}')
    return

if __name__ == '__main__':
    main()