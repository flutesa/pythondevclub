# Desc sorting
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j + 1] > a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = list(map(int, input().split()))
a = BubbleSort(a)
print(' '.join(list(map(str, a))))
