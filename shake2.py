n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
while left < right:
    for i in range(left, right):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    right -= 1
    for j in range(right, left, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
    left += 1
print(*a)