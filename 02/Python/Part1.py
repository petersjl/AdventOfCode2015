from pathlib import Path

def parseInput():
    path = Path(__file__).parent / "../input.txt"
    input = path.open().read()
    # split each line
    objs = input.split("\n")
    list = []
    # split each object on the x's and then save values to a touple
    for o in objs:
        obj = o.split("x")
        list.append((int(obj[0]), int(obj[1]), int(obj[2])))
    return list

def main():
    input = parseInput()
    area = 0
    for present in input:
        # get the face areas of each present
        (l, w, h) = present
        lw = l * w
        lh = l * h
        wh = w * h
        curArea = 2*lw + 2*lh + 2*wh
        if lw < lh:
            if lw < wh: curArea += lw
            else: curArea += wh
        else:
            if lh < wh: curArea += lh
            else: curArea += wh
        print(f'{l}x{w}x{h} -> {curArea}')
        area += curArea
    print(f'\nTotal area: {area}')
    return

if __name__ == '__main__':
    main()