from pathlib import Path
from time import perf_counter as timer

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = list(map(lambda x: x.split(" "), path.open().read().split("\n")))
    input.sort(key=lambda x: len(x))
    return input

def main():
    input = parseInput()
    wires = {}
    i = 0
    while len(input) > 0:
        if len(input) == 0: break
        if i == len(input): i = 0
        current = input[i]
        # print(f'{i}: {current}')
        # Current instruction is a single assignment
        if len(current) == 3:
            if current[0].isnumeric():
                wires[current[2]] = toBinString(current[0])
                print(f'{i}: {current}')
                input.pop(i)
            else:
                if wires.get(current[0]):
                    wires[current[2]] = wires[current[0]]
                    print(f'{i}: {current}')
                    input.pop(i)
                else: i += 1
        # Current command is a not
        elif len(current) == 4:
            num:str
            if current[1].isnumeric():
                num = toBinString(current[1])
            elif wires.get(current[1]):
                num = wires[current[1]]
            else: 
                i += 1
                continue
            num = bNot(num)
            wires[current[3]] = num
            print(f'{i}: {current}')
            input.pop(i)
        # Current command has two inputs
        elif len(current) == 5:
            first:str = parseVal(current[0], wires)
            if first == None:
                i += 1
                continue
            if current[1] == "AND": 
                second = parseVal(current[2], wires)
                if second == None:
                    i += 1
                    continue
                wires[current[4]] = bAnd(first,second)
            elif current[1] == "OR": 
                second = parseVal(current[2], wires)
                if second == None:
                    i += 1
                    continue
                wires[current[4]] = bOr(first,second)
            elif current[1] == "LSHIFT": wires[current[4]] = lshift(first, int(current[2]))
            elif current[1] == "RSHIFT": wires[current[4]] = rshift(first, int(current[2]))
            else:
                print(f'Unknown command: {current[1]}')
                exit()
            print(f'{i}: {current}')
            input.pop(i)
        else:
            print("Malformed command")
    print(f'The a wire has value {binToInt(wires["a"])}')
    return

def toBinString(num:str) -> str:
    num = str(bin(int(num)))[2:]
    while len(num) != 16:
        num = "0" + num
    return num

def binToInt(num:str) -> int:
    return int(num, 2)

def parseVal(string, wires) -> str:
    if string.isnumeric():
        return toBinString(string)
    elif wires.get(string):
            return wires[string]
    else:
        return None

def bAnd(num1:str, num2:str) -> str:
    out = ""
    for i in range(16):
        out += "1" if num1[i]=="1" and num2[i]=="1" else "0"
    return out

def bOr(num1:str, num2:str) -> str:
    out = ""
    for i in range(16):
        out += "1" if num1[i]=="1" or num2[i]=="1" else "0"
    return out

def bNot(num:str) -> str:
    out = ""
    for i in range(16):
        out += "1" if num[i]=="0" else "0"
    return out

def lshift(num:str, count:int) -> str:
    for _ in range(count):
        num = num[1:]
        num += "0"
    return num

def rshift(num:str, count:int) -> str:
    for _ in range(count):
        num = num[:-1]
        num = "0" + num
    return num

if __name__ == '__main__':
    start = timer()
    main()
    end = timer()
    print(f'Ran in {end - start} seconds')