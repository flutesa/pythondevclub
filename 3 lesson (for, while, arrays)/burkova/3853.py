array = list(map(int, input().split()))
k = int(input())

if k > 0:
    k = (-k) % len(array)

    i = 0
    j = k - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

    i = k
    j = len(array) - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

    i = 0
    j = len(array) - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

if k < 0:
    k = k % len(array)

    i = 0
    j = len(array) - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

    i = 0
    j = k - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

    i = k
    j = len(array) - 1
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1

print(' '.join(list(map(str, array))))

