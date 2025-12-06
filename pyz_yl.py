n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(1, n):
    for j in range(len(a) - 1, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            k += 1
    if k == 0:
        break
print(*a)