from pprint import pprint as pp 
range_str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

with open("part01_input.txt","r") as f:
    range_str = f.read().strip()

range_list = range_str.split(",")
ranges = [tuple(map(int, r.split("-"))) for r in range_list]
pp(ranges)

acc = 0 
count = 0
for (r_start,r_end) in ranges:
    print(f"Range from {r_start} to {r_end} has {r_end - r_start + 1} numbers.")
    min_len = len(str(r_start))
    max_len = len(str(r_end))
    for length in range(min_len, max_len + 1):
        if length % 2 == 0: # can't be a repeat if it isn't even
            if length > min_len: # start at 10..0 since we can't have leading zeros
                cur_digits = "1" + "0" * (length//2 - 1)
            else:
                cur_digits = str(r_start)[:length//2]
            print(f"  Starting at {cur_digits} for length {length}")
            num = int(cur_digits+cur_digits)
            while num <= r_end and len(str(num)) == length:
                if num >= r_start:
                    print(f"  Found bad ID: {num}")
                    count = count + 1
                    acc = acc + num
                cur_digits = str(int(cur_digits) + 1)
                num = int(cur_digits+cur_digits)
print(f"count: {count} acc: {acc}")

                
