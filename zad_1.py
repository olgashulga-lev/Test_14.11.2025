import random

def task1(num):
    min_sum = 10000
    for j in range(0, len(num) - 1):
        summa = num[j] + num[j + 1]
        if summa <= min_sum:
            min_sum = summa
            ind1 = j + 1
            ind2 = j + 2
    return ind1, ind2

def test_task1():
    if task1([0, 1, 2]) == (1, 2):
        print("+")
    else:
        print(f"Error, для списка [0, 1, 2] ожидается 1, 2, а у вас")
    if task1([5, 4, 5, 4]) == (3, 4):
        print("+")
    else:
        print(f"Error, для списка [5, 4, 5, 4] ожидается 3, 4, а у вас")
    if task1([3, 1, 5, -2]) == (3, 4):
        print("+")
    else:
        print(f"Error, для списка [3, 1, 5, -2] ожидается 3, 4, а у вас")
    if task1([5, 4, 5, 4, 5, 4, 5, 4]) == (7, 8):
        print("+")
    else:
        print(f"Error, для списка [5, 4, 5, 4, 5, 4, 5, 4] ожидается 7, 8, а у вас")
    if task1([5, 1, 1, 4]) == (2, 3):
        print("+")
    else:
        print(f"Error, для списка [5, 1, 1, 4] ожидается 2, 3, а у вас")
    if task1([-5, -1, 1, 4]) == (1, 2):
        print("+")
    else:
        print(f"Error, для списка [-5, -1, 1, 4] ожидается 1, 2, а у вас")


print(task1([0, 1, 2, -2]))
test_task1()
n = int(input())
a = int(input())
b = int(input())
num = [0] * n
min_sum = 100000
for i in range(n):
    num[i] = random.randint(a, b)
print(num)
for j in range(0, n - 1):
    summa = num[j] + num[j + 1]
    if summa <= min_sum:
        min_sum = summa
        ind1 = j + 1
        ind2 = j + 2
print(ind1)
print(ind2)