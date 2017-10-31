from collections import Counter
if __name__ == "__main__":
    s = raw_input().strip()
    d = Counter(s)
    mc = d.most_common(3)
    for i in sorted(mc, key = lambda x: (-x[1], x[0]))[:3]:
        print(" ".join(map(str, i)))