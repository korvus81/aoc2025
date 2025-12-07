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

def merge_beams(beams):
    new_beams = {}
    for (beamx,timelines) in beams:
        new_beams[beamx] = new_beams.get(beamx,0) + timelines
    return sorted(list(new_beams.items()))


def main():
    lines,start = parse_input(input_str)
    pp(lines)
    print(start)
    #marked_up = []
    splits = 0
    beams = [(start[1],1)] # assuming start row is 0, start with one timeline
    for rownum,row in enumerate(lines):
        newbeams = []
        if rownum == 0:
            #marked_up.append(row)
            continue
        for (col,beamtimelines) in beams:
            if lines[rownum][col] == "^":
                splits += 1
                if col-1 >= 0:
                    newbeams.append((col-1,beamtimelines))
                if col+1 < len(row):
                    newbeams.append((col+1,beamtimelines))
            else:
                newbeams.append((col,beamtimelines))
        #newrow = [(c if cnum not in newbeams else '|') for cnum,c in enumerate(row)]
        #marked_up.append(newrow)
        beams = merge_beams(newbeams)
        #beams = sorted(list(set(newbeams)))
    print(splits)
    pp(beams)
    timelines = sum([tlines for (c,tlines) in beams])
    print(f"Timelines = {timelines}")
    

if __name__ == "__main__":
    main()
