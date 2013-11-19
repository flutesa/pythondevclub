n = int(input())
a = []
maths_expectance = 0
difference = 0
maximum_prbbl = 0
minimum_prbbl = 1
maximum = 0
minimum = 0
is_maths_expectance = 0

n = n * 2

for i in range(n):
    if i % 2 == 0:
        a.append(int(input()))
    else:
        a.append(float(input()))

for i in range(n):
    if i % 2 == 0:
        maths_expectance = maths_expectance + a[i] * a[i + 1]

print('M[X] = ', maths_expectance)

for i in range(n):
    if i % 2 != 0:
        if a[i] > maximum_prbbl:
            maximum_prbbl = a[i]
            maximum = a[i-1]
        elif a[i] < minimum_prbbl:
            minimum_prbbl = a[i]
            minimum = a[i-1]

print('Разность самого вероятного и самого маловероятного чисел: ', maximum - minimum)

for i in a:
    if i == maths_expectance:
        is_maths_expectance = is_maths_expectance + 1

if is_maths_expectance == 0:
    print('NO')
else:
    print('YES')
