def task2(a):
    pol = []
    zero = []
    otr = []
    for i in range(0, len(a)):
        if a[i] > 0:
            pol.append(a[i])
        elif a[i] == 0:
            zero.append(a[i])
        else:
            otr.append(a[i])
    res = pol + zero + otr
    return res

def test_task2():
    if task2([-6, 2, 0]) == [2, 0, -6]:
        print('+')
    else:
        print(f"Ошибка, должно быть [2, 0, -6], а у вас {task2([-6, 2, 0])}")
    if task2([-5, -9, -4, 0, -3]) == [0, -5, -9, -4, -3]:
        print('+')
    else:
        print(f"Ошибка, должно быть [0, -5, -9, -4, -3], а у вас {task2([-5, -9, -4, 0, -3])}")
    if task2([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]:
        print('+')
    else:
        print(f"Ошибка, должно быть [5, 4, 3, 2, 1], а у вас {task2([5, 4, 3, 2, 1])}")
    if task2([-3, -4, -7, -9]) == [-3, -4, -7, -9]:
        print('+')
    else:
        print(f"Ошибка, должно быть [-3, -4, -7, -9], а у вас {task2([-3, -4, -7, -9])}")
    if task2([0, 0, 0, 1, -1]) == [1, 0, 0, 0, -1]:
        print('+')
    else:
        print(f"Ошибка, должно быть [0, 0, 0, 1, -1], а у вас {task2([0, 0, 0, 1, -1])}")

test_task2()
print(task2([-6, 2, 0]))
a = list(map(int, input().split()))
pol = []
zero = []
otr = []
for i in range(0, len(a)):
    if a[i] > 0:
        pol.append(a[i])
    elif a[i] == 0:
        zero.append(a[i])
    else:
        otr.append(a[i])
res = pol + zero + otr
print(res)