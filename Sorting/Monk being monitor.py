from collections import Counter

for _ in range(int(input())):
    input()
    l = Counter(input().split()).values()
    val = max(l) - min(l)
    print(val if val else -1)
