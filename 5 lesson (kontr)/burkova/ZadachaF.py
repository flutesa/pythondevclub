def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def find_me(a, b):
    max_element = b
    index = a.index(a[0])
    for i in range(len(a)):
        if a[i] >= max_element:
            index = i + 1
    return index


array = list(map(int, input().split()))
element = int(input())

array.append(element)

bubble_sort(array)

print(find_me(array, element))
