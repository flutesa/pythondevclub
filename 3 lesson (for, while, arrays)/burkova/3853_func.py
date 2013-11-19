def reverse(array, start, stop):
    i = start
    j = stop
    while i < j:
        buffer = array[i]
        array[i] = array[j]
        array[j] = buffer
        i += 1
        j -= 1


def shift(array, k):
    if k > 0:
        k = (-k) % len(array)
        reverse(array, 0, k-1)
        reverse(array, k, len(array) - 1)
        reverse(array, 0, len(array) - 1)
    if k < 0:
        k = k % len(array)
        reverse(array, 0, len(array) - 1)
        reverse(array, 0, k-1)
        reverse(array, k, len(array) - 1)

a = [5, 3, 7, 4, 6]
shift(a, 3)
print(' '.join(list(map(str, a))))
b = [1, 2, 3, 4, 5]
shift(b, -1)
print(' '.join(list(map(str, b))))
b = [1, 2, 3, 4, 5]
shift(b, -2)
print(' '.join(list(map(str, b))))
b = [1, 2, 3, 4, 5]
shift(b, -3)
print(' '.join(list(map(str, b))))
b = [1, 2, 3, 4, 5]
shift(b, -4)
print(' '.join(list(map(str, b))))
b = [1, 2, 3, 4, 5]
shift(b, -5)
print(' '.join(list(map(str, b))))