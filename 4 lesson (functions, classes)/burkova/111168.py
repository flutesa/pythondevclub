def flavius(n, k):
    p = []
    for i in range(n):
        p.append(i+1)
    i = 0
    seq = []
    while p:
        i = (i+k-1) % len(p)
        seq.append(p.pop(i))
    return seq[-1]


a = list(map(int, input().split()))

print(flavius(a[0], a[1]))