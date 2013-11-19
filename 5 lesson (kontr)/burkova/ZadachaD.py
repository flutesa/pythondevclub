a = int(input())
b = int(input())

if (a == 1 and b == 1) or (a != b and b != 1 and a != 1):
    print('YES')
elif (a != b and b == 1) or (a != b and a == 1):
    print('NO')
else:
    print('YES')
