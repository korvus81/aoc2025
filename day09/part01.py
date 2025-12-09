from pprint import pprint as pp 


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

best_points = []
max_area = 0

for point in points:
    x1, y1 = point
    print(f"Point: x={x1}, y={y1}")
    for other_point in points:
        if other_point == point:
            continue
        x2, y2 = other_point
        area = (abs(x2 - x1)+1) * (abs(y2 - y1) +1)
        if area > max_area:
            max_area = area
            best_points = [(point, other_point, area)]
        print(f"  Other Point: x={x2}, y={y2}, Area={area}")

print("Best Points and Area:")
pp(best_points)
pp(max_area)