a = list(map(int, input().split())) 
counter = 0

for i in a:
    if i > 0:
        counter += 1
        
print(counter)
