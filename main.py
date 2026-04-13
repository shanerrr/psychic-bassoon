import sys

def is_safe(levels):
    increasing = True
    decreasing = True
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if diff < 1 or diff > 3:
            increasing = False
        if diff > -1 or diff < -3:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True

def is_safe_dampened(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1:]):
            return True
    return False

count_p1 = 0
count_p2 = 0
for line in open(sys.argv[1] if len(sys.argv) > 1 else "input.txt"):
    levels = list(map(int, line.split()))
    if not levels:
        continue
    if is_safe(levels):
        count_p1 += 1
        count_p2 += 1
    elif is_safe_dampened(levels):
        count_p2 += 1

print(f"Part 1: {count_p1}")
print(f"Part 2: {count_p2}")
