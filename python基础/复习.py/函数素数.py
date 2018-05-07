A = []
for i in range(100,1001):
    mark = 0
    for j in range(2,i):
        if i%j == 0:
            make = 1
            break
    if make == 0:
        A.append(i)
print(A)

