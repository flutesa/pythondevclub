n = int(input())

a = list(map(int, input().split()))

a.reverse()

print('\n'.join(list(map(str, a))))