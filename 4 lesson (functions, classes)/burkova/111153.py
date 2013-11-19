def LastMax(a):
    max_element = a[0]
    index = a.index(a[0])
    for i in range(len(a)):
        if a[i] >= max_element:
            max_element = a[i]
            index = i
    return max_element, index

a = list(map(int, input().split()))
answer = LastMax(a)
print(answer[0], answer[1])
