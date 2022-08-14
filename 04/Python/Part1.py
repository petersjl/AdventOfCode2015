from pathlib import Path
from hashlib import md5 as hash

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open()
    return input.read()

def main():
    input = parseInput()
    result = False
    num = 0
    while not result:
        num += 1
        result = checkHash(input, num)
    print(f'The magic number is {num}')
    return

def checkHash(string, num):
    code = string + str(num)
    result = hash(code.encode()).hexdigest()
    print(f'{num} : {result}')
    result = str(result)
    index = 0
    for c in result:
        if not c == '0': return False
        index += 1
        if index == 5: return True

if __name__ == '__main__':
    main()