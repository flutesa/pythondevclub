'''
This programm is example of how to use and write bubble sort.
Interface - how does it works from user's point of view:
console]>python3 2.py
1 4 5 3 2
1 2 3 4 5
console]>python3 2.py
5 4 3 2 1
1 2 3 4 5
console]>python3 2.py
1 2 3 4 5
1 2 3 4 5
console]>python3 2.py
1 5 2 4 3 6 9 7 8
1 2 3 4 5 6 7 8 9
'''

def bubble_sort(a):
    '''
    This function recives array a.
    It returnes sorted array a.
    Time of it's working is O(n^2)
    '''
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = list(map(int, input().split()))
a = bubble_sort(a)
print(' '.join(list(map(str, a))))
