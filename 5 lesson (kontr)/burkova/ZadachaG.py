def have_unsafe_pos(a, b):
    for i in range(8):
        for j in range(i + 1, 8):
            if (a[i] == a[j]) or (b[i] == b[j]) or (abs(a[i] - a[j]) == abs(b[i] - b[j])):
                return "YES"
    return "NO"


array_i = [0] * 8
array_j = [0] * 8

for i in range(8):
    array_i[i], array_j[i] = list(map(int, input().split(" ")))

print(have_unsafe_pos(array_i, array_j))