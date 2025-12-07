from pprint import pprint as pp


input_str = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

with open("part01_input.txt") as f:
    input_str = f.read()


def parse_input(input_str):
    lines = [list(line.strip()) for line in input_str.split("\n")]
    for rownum,row in enumerate(lines):
        for colnum,col in enumerate(row):
            if col == "S":
                start = (rownum, colnum)

    return lines,start


def main():
    lines,start = parse_input(input_str)
    pp(lines)
    print(start)
    marked_up = []
    splits = 0
    cols = [start[1]] # assuming start row is 0
    for rownum,row in enumerate(lines):
        newcols = []
        if rownum == 0:
            marked_up.append(row)
            continue
        for col in cols:
            if lines[rownum][col] == "^":
                splits += 1
                if col-1 >= 0:
                    newcols.append(col-1)
                if col+1 < len(row):
                    newcols.append(col+1)
            else:
                newcols.append(col)
        newrow = [(c if cnum not in newcols else '|') for cnum,c in enumerate(row)]
        marked_up.append(newrow)
        cols = sorted(list(set(newcols)))
    print(splits)
    pp(cols)

    print()
    for row in marked_up:
        print("".join(row))
    print()

if __name__ == "__main__":
    main()
