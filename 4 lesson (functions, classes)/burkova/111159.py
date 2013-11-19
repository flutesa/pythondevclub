def bubble_sort_asc(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def users_max_zip(requirements, users_data):

    bubble_sort_asc(users_data)

    summ = 0
    count = 0
    for q in users_data:
        while (summ + q) <= requirements[0]:
            summ += q
            count += 1
            break

    return count


a = list(map(int, input().split(" ")))

b = []
for i in range(int(a[1])):
    b.append(int(input()))


print(users_max_zip(a, b))

