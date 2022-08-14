from pathlib import Path
from time import perf_counter as timer

class Instruction:
    def __init__(self, command, start, end):
        self.command = command
        self.start = start
        self.end = end

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open().read().split("\n")
    instructions = []
    for s in input:
        parts = s.split(" ")
        i: Instruction
        if len(parts) == 5:
            i = Instruction(
                parts[1],
                parts[2],
                parts[4]
            )
        else:
            i = Instruction(
                parts[0],
                parts[1],
                parts[3]
            )
        instructions.append(i)
    return instructions

def main():
    input = parseInput()
    lights = [ [False]*1000 for i in range(1000)]
    for i in input:
        start = list(map(lambda x: int(x), i.start.split(",")))
        end = list(map(lambda x: int(x), i.end.split(",")))
        func: function
        if i.command == "toggle": func = lambda x: not x
        elif i.command == "on": func = lambda x: True
        else: func = lambda x: False
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                lights[x][y] = func(lights[x][y])
    count = 0
    for x in lights:
        for y in x:
            if y: count += 1
    print(f'Lights turned on: {count}')
    return

if __name__ == '__main__':
    start = timer()
    main()
    end = timer()
    print(f'Ran in {end - start} seconds')