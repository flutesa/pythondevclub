def bubble_sort_asc(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


f = open('111167.txt', 'r')

n = int(f.readline())
kb_durability = list(map(int, f.readline().split(" ")))

k = int(f.readline())
sq_typing = list(map(int, f.readline().split(" ")))
f.close()

sq_typing = bubble_sort_asc(sq_typing)


#for i in range(n):
#    if sq_typing.count(i+1) > kb_durability[i]:
#        print("YES")
#    else:
#        print("NO")

# относительно верно
sq_typing_summ = [[0] * 2 for i in range(n)]
count = 0
oldvalue = sq_typing[0]
i = 1
for i in range(n):
    if sq_typing[i] == oldvalue:
        count += 1
    else:
        sq_typing_summ[0][i] = oldvalue
        sq_typing_summ[1][i] = count
        count = 1

print(''.join(list(map(str, sq_typing_summ))))
#print(sq_typing.count(1))
#print(sq_typing.count(2))
#print(sq_typing.count(3))
#print(sq_typing.count(4))
#print(sq_typing.count(5))

#sq_typing_summ = []
#summ = 0
#j = 1
#for i in range(len(kb_durability)):
#    for j in range(len(sq_typing)):
#        if sq_typing[j-1] - sq_typing[j] == 0:
#            summ += 1
#            print(summ)
#        elif sq_typing[j + 1] - sq_typing[j-1] - sq_typing[j] == 0:
#            summ = 1
#        else:
#            summ = 0
#    sq_typing_summ.append(summ)
#    summ = 0


#sq_typing_summ = []
#summ = 0
#i = 0
#for i in range(len(kb_durability)):
#    summ = 0
#    for j in range(len(sq_typing)):
#        while kb_durability[i] == sq_typing[j]:
#            summ += 1
#            print(summ)
#            break
#    sq_typing_summ.append(summ)



# относительно верно
#sq_typing_summ = []
#summ = 0
#for i in range(n):
#    for j in range(k):
#        while kb_durability[i] == sq_typing[j]:
#            summ += 1
#            print(summ)
#            break
#    sq_typing_summ.append(summ)
#    summ = 0


#совсем не верно
#sq_typing_summ = []
#summ = 0
#
#for i in range(k):
#    for j in range(n):
#        summ = 0
#        while kb_durability[j] == sq_typing[i]:
#            summ += 1
#            #print(summ)
#            break
#    sq_typing_summ.append(summ)








#
#
#result = [n]

#for i in range(n):
#    print('\n'.join(list(map(str, result))))





#sq_typing_summ = [k]
#summ = 0

#i = 1
#for i in range(k):
#    if sq_typing[i] == sq_typing[i-1]:
#        summ += 1
#    print(summ)

http://forum.searchengines.ru/showthread.php?t=276055