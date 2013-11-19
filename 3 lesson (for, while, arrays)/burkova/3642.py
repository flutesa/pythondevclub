n = int(input())
a = []
max_n = 1

for i in range(n):
    max_n = i*i
    if max_n > n:
        break
    elif n == 1:
        a.append(1)
    elif i == 0:       
        continue
    else:
        a.append(max_n)

print(' '.join(list(map(str, a))))
