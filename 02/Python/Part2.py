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

def perimeter(x, y):
    return 2*x + 2*y

def main():
    input = parseInput()
    area = 0
    ribbon = 0
    for present in input:
        # get the face areas of each present
        (l, w, h) = present
        lw = l * w
        lh = l * h
        wh = w * h
        curArea = 2*lw + 2*lh + 2*wh
        curRibbon = 0
        if lw < lh:
            if lw < wh: 
                curArea += lw
                curRibbon += perimeter(l, w)
            else: 
                curArea += wh
                curRibbon += perimeter(w, h)
        else:
            if lh < wh: 
                curArea += lh
                curRibbon += perimeter(l, h)
            else: 
                curArea += wh
                curRibbon += perimeter(w, h)
        curRibbon += l*w*h
        print(f'{l}x{w}x{h} -> Paper: {curArea}sqft / Ribbon: {curRibbon}ft')
        area += curArea
        ribbon += curRibbon
    print(f'\nTotal paper: {area}\nTotal ribbon: {ribbon}')
    return

if __name__ == '__main__':
    main()