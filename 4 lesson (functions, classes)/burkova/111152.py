def IsAscending(a):
    i = 1
    step = 1

    while i < len(a) and step > 0:
        step = a[i] - a[i-1]
        i += 1
 
    if step > 0:
        return "YES"
    else:
        return "NO"
 
 
a = list(map(int, input().split()))
print(IsAscending(a))