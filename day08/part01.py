from pprint import pprint as pp 
import math 
import time 
from scipy.cluster.hierarchy import DisjointSet

input_str = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

CONNECTIONS = 10 

with open("part01_input.txt") as f:
    input_str = f.read()
    CONNECTIONS = 1000

def parse_input(input_str):
    lines = input_str.strip().split("\n")
    points = [tuple(map(int, line.split(","))) for line in lines]
    return points # list of (x,y,z) tuples

points = parse_input(input_str)
pp(points)

def distance(x1,x2,y1,y2,z1,z2):
    # power of 1/3 -> cube root 
    return math.pow((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2,1/3)


point_pairs_and_distances = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        if i != j:
            p1 = points[i]
            p2 = points[j]
            dist = distance(p1[0], p2[0], p1[1], p2[1], p1[2], p2[2])
            if p1 < p2:
                point_pairs_and_distances.append((p1, p2, dist))
            else:
                point_pairs_and_distances.append((p2, p1, dist))
point_pairs_and_distances.sort(key=lambda x: x[2])
pp(point_pairs_and_distances)


ds = DisjointSet(points)
for i in range(CONNECTIONS):
    p1, p2, dist = point_pairs_and_distances[i]
    print(f"Connecting {p1} to {p2} with distance {dist}")
    ds.merge(p1, p2)

subsets = sorted(ds.subsets(), key=lambda x: len(x), reverse=True)
pp(subsets)
print(f"Number of constellations: {len(subsets)}")
top3sizes = [len(subsets[i]) for i in range(3)]
print(f"Top 3 largest constellations sizes: {top3sizes} (multiplied {top3sizes[0]*top3sizes[1]*top3sizes[2]})")