import math
from pprint import pprint as pp 
range_str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

with open("part01_input.txt","r") as f:
    range_str = f.read().strip()

range_list = range_str.split(",")
ranges = [tuple(map(int, r.split("-"))) for r in range_list]
pp(ranges)

found_set = set() # easiest way to avoid repeats
acc = 0 
count = 0
for (r_start,r_end) in ranges:
    print(f"\nRange from {r_start} to {r_end} has {r_end - r_start + 1} numbers.")
    min_len = len(str(r_start))
    max_len = len(str(r_end))
    for length in range(min_len, max_len + 1):
        # this was obnoxious to figure out
        possible_repeat_amounts = list(range(2,math.ceil(length / 2)+2))
        #print(math.ceil(length / 2)+2)
        #pp(possible_repeat_amounts)
        for repeat_amount in possible_repeat_amounts:
            print(f"  Checking repeat amount: {repeat_amount}")
            if length % repeat_amount == 0: # can't be a repeat if it isn't an even multiple
                print(f"    Length {length} is divisible by {repeat_amount}")
                sub_length = length // repeat_amount
                if length > min_len: # start at 10..0 since we can't have leading zeros
                    cur_digits = "1" + "0" * (sub_length - 1)
                else:
                    cur_digits = str(r_start)[:sub_length]
                print(f"  Starting at {cur_digits} for length {length}")
                num = int(cur_digits * repeat_amount)
                while num <= r_end and len(str(num)) == length:
                    if num >= r_start and num not in found_set:
                        print(f"  *** Found bad ID: {num} ***")
                        count = count + 1
                        acc = acc + num
                        found_set.add(num)
                    cur_digits = str(int(cur_digits) + 1)
                    num = int(cur_digits * repeat_amount)
pp(found_set)
print(f"count: {count} acc: {acc}")
# 36020474820 is too low


import re 
# stupid brute force solution.
count = 0
acc = 0
for (r_start,r_end) in ranges:
    print(f"\nRange from {r_start} to {r_end} has {r_end - r_start + 1} numbers.")
    for num in range(r_start, r_end + 1):
        num_str = str(num)
        length = len(num_str)
        pattern = r"^([0-9]+)\1+$"
        if re.match(pattern, num_str):
            print(f"  *** Found bad ID by brute force: {num} ***")
            count = count + 1
            acc = acc + num
print(f"count: {count} acc: {acc}")
# found 36037497037
                
