import itertools
import collections


def in_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n


def get_antinodes(a, b, n):
    ax, ay = a
    bx, by = b
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)

    if in_bounds(cx, cy, n):
        yield (cx, cy)
    if in_bounds(dx, dy, n):
        yield (dx, dy)


def main():
    with open("input_08_12.txt", "r") as f:
        data = f.read().strip().split("\n")

    print(data)
    n = len(data)
    print(n)
    all_locs = collections.defaultdict(list)
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1):
            if data[i][j] != ".":
                all_locs[data[i][j]].append((i, j))
    antinodes = []
    for freq in all_locs:
        locs = all_locs[freq]
        for a, b in itertools.combinations(locs, r=2):
            for antinode in get_antinodes(a, b, n):
                print("this is antinode", antinode)
                antinodes.append(antinode)
    print(len(antinodes))
    print(len(set(antinodes)))


if __name__ == "__main__":
    main()
