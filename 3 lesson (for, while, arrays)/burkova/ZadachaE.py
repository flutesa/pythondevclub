n = int(input())
a = list(map(int, input().split()))

n = n - 1
b = list(map(int, input().split()))

for i in b:
    for j in a:
        if i == j:
            a.remove(i)

print(' '.join(list(map(str, a))))
