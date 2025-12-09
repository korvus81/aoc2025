# This file is a disaster.  Enter at your own risk.

from pprint import pprint as pp 
import os
import sys 
from rich.pretty import pprint as pp
# https://rich.readthedocs.io/en/latest/markup.html#console-markup
from rich import print as p

input_str = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

with open("part01_input.txt") as f:
    input_str = f.read().strip()

points = [tuple(map(int, line.split(","))) for line in input_str.splitlines()]
pp(points)

## this was to validate the coordinates alternate horiz/vert
# horiz = None  
# pairs = zip(points[0:-1], points[1:])
# for p1, p2 in pairs:
#     if horiz is None:
#         if p1[0] == p2[0]:
#             horiz = False # xs match, so ys differ
#         else:
#             horiz = True # ys match, so xs differ
#     elif horiz: # last had matching ys (xs differ), so this should have matching xs
#         if p1[0] != p2[0]:
#             print(f"Error: expected vertical line {p1} to {p2}")
#             sys.exit()
#         else:
#             horiz = False
#     else:
#         if p1[1] != p2[1]:
#             print(f"Error: expected horizontal line {p1} to {p2}")
#             sys.exit()
#         else: 
#             horiz = True
# print("all was well")
# sys.exit()

main_edges = list(zip(points[:], points[1:]+[points[0]]))
main_horiz_edges = [edge for edge in main_edges if edge[0][1] == edge[1][1]]
main_vert_edges = [edge for edge in main_edges if edge[0][0] == edge[1][0]]

best_points = []
max_area = 0

def check_for_crosses(main_horiz_edges, main_vert_edges, test_horiz_edges, test_vert_edges):
    for e in main_horiz_edges:
        for e2 in test_vert_edges:
            
            # if e starts left of the vertical edge and ends right of the vertical edge
            vert_edge_xpos = e2[0][0] # should be the same for both points
            e_crosses_x_coord = (min(e[0][0],e[1][0]) <= vert_edge_xpos) and (max(e[0][0],e[1][0]) >= vert_edge_xpos)
            horiz_edge_ypos = e[0][1] # should be the same for both points
            e_in_y_range = horiz_edge_ypos > min(e2[0][1], e2[1][1]) and horiz_edge_ypos < max(e2[0][1], e2[1][1])
            if e_crosses_x_coord and e_in_y_range:
                return True
    for e in main_vert_edges:
        for e2 in test_horiz_edges:        
            # if e starts above the horizontal edge and ends below the horizontal edge
            horiz_edge_ypos = e2[0][1] # should be the same for both points
            e_crosses_y_coord = (min(e[0][1],e[1][1]) <= horiz_edge_ypos) and (max(e[0][1],e[1][1]) >= horiz_edge_ypos)
            vert_edge_xpos = e[0][0] # should be the same for both points
            e_in_x_range = vert_edge_xpos > min(e2[0][0], e2[1][0]) and vert_edge_xpos < max(e2[0][0], e2[1][0])
            if e_crosses_y_coord and e_in_x_range:
                return True
    return False

def check_for_crosses2(points, p1,p2):
    p1x, p1y = p1
    p2x, p2y = p2
    minx = min(p1x, p2x)
    maxx = max(p1x, p2x)
    miny = min(p1y, p2y)
    maxy = max(p1y, p2y)
    for pt in points:
        if pt == p1 or pt == p2:
            continue
        ptx, pty = pt
        if ptx > minx and ptx < maxx and pty > miny and pty < maxy:
            return True
        if ptx == minx and pty > miny and pty < maxy:
            return True
        if ptx == maxx and pty > miny and pty < maxy:
            return True
        if pty == miny and ptx > minx and ptx < maxx:
            return True
        if pty == maxy and ptx > minx and ptx < maxx:
            return True
    return False


def check_for_crosses3(main_horiz_edges, main_vert_edges, p1, p2):
    minx = min(p1[0], p2[0])
    maxx = max(p1[0], p2[0])
    miny = min(p1[1], p2[1])
    maxy = max(p1[1], p2[1])
    for e in main_horiz_edges:
        horiz_edge_ypos = e[0][1] # should be the same for both points
        horiz_edge_minx = min(e[0][0], e[1][0])
        horiz_edge_maxx = max(e[0][0], e[1][0])
        if horiz_edge_ypos > miny and horiz_edge_ypos < maxy:
            if horiz_edge_maxx > minx and horiz_edge_minx < maxx:
                return True
        
    for e in main_vert_edges:
        vert_edge_xpos = e[0][0] # should be the same for both points
        vert_edge_miny = min(e[0][1], e[1][1])
        vert_edge_maxy = max(e[0][1], e[1][1])
        if vert_edge_xpos > minx and vert_edge_xpos < maxx:
            if vert_edge_maxy > miny and vert_edge_miny < maxy:
                return True
    return False

base_map = []
max_x = max(x for x,y in points)
max_y = max(y for x,y in points)

can_draw = False
if max_x < 50 and max_y < 50:
    can_draw = True
if can_draw:
    for y in range(max_y+2):
        row = []
        for x in range(max_x+2):
            if (x,y) in points:
                row.append("[red]#[/red]")
                continue
            is_edge = False 
            is_vedge = False
            is_hedge = False 
            for edge in main_horiz_edges:
                if (y == edge[0][1]) and (x >= min(edge[0][0], edge[1][0])) and (x <= max(edge[0][0], edge[1][0])):
                    is_edge = True
                    is_hedge = True
            for edge in main_vert_edges:
                if (x == edge[0][0]) and (y >= min(edge[0][1], edge[1][1])) and (y <= max(edge[0][1], edge[1][1])):
                    is_edge = True
                    is_vedge = True
            if is_edge:
                if is_hedge and is_vedge: # probably always a point, but just in case
                    row.append("[blue]+[/blue]")
                elif is_hedge:
                    row.append("[green]-[/green]")
                else:
                    row.append("[green]|[/green]")
            else:
                row.append("[white].[/white]")
        base_map.append(row)

def print_map(base_map,p1,p2):
    display_map = [row[:] for row in base_map]
    display_map[p1[1]][p1[0]] = "[yellow]A[/yellow]"
    display_map[p2[1]][p2[0]] = "[yellow]B[/yellow]"
    for row in display_map:
        p("".join(row))
    p("")

if can_draw:
    print()
    print()

    for row in base_map:
        p("".join(row))
    p("")



for point in points:
    x1, y1 = point
    print(f"Point: x={x1}, y={y1}")
    for other_point in points:
        if other_point == point:
            continue
        x2, y2 = other_point
        area = (abs(x2 - x1)+1) * (abs(y2 - y1) +1)
        if area < max_area:
            continue # optimization to skip all the intersection tests

        horiz_edges = [((x1, y1),(x2,y1)), ((x1, y2), (x2,y2))]
        vert_edges = [((x1, y1),(x1,y2)), ((x2, y1), (x2,y2))]
        
        #crossed = check_for_crosses(main_horiz_edges, main_vert_edges, horiz_edges, vert_edges)
        #crossed = check_for_crosses2(points, point, other_point)
        crossed = check_for_crosses3(main_horiz_edges, main_vert_edges, point, other_point)
        if not crossed:
            if area > max_area:
                max_area = area
                best_points = [(point, other_point, area)]
            print(f"  Other Point: x={x2}, y={y2}, Area={area}")
            if can_draw:
                print_map(base_map, point, other_point)
            

print("Best Points and Area:")
pp(best_points)
pp(max_area) 
# not 2894419625
# not 1363080015 -- too low
# not 4525501422 -- too high
# it is 1468516555!
