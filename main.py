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

count = 0
for line in open(sys.argv[1] if len(sys.argv) > 1 else "input.txt"):
    levels = list(map(int, line.split()))
    if levels and is_safe(levels):
        count += 1

print(count)
