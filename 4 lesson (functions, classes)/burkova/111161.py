def bubble_sort_dsc(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j + 1][1] > a[j][1]:
                a[j][0], a[j + 1][0] = a[j + 1][0], a[j][0]
                a[j][1], a[j + 1][1] = a[j + 1][1], a[j][1]
    return a


n = int(input())

b = [[0] * 2 for i in range(n)]
buffer = []
for i in range(n):
    buffer = input().split(" ")
    b[i][0] = buffer[0]
    b[i][1] = buffer[1]

b = bubble_sort_dsc(b)

for i in range(n):
    str(b[i][0]).split()
    print(b[i][0])