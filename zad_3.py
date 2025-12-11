def Longest_word(S):
    words = S.split()
    if not words:
        return ""
    long_word = words[0]
    max_length = 0
    for i in long_word:
        max_length += 1
    for word in words:
        tek_word = 0
        for j in word:
            tek_word += 1
        if tek_word > max_length:
            max_length = tek_word
            long_word = word
    return long_word


def test_task2():
    if Longest_word('Я ничего не понимаю') == 'понимаю':
        print('+')
    else:
        print(
            f"Неверно, для строки 'Я ничего не понимаю' ожидается 'понимаю', а у вас {Longest_word('Я ничего не понимаю')}")
    if Longest_word('люблю знают') == 'люблю':
        print('+')
    else:
        print(f"Неверно, для строки 'люблю знают' ожидается 'люблю', а у вас {Longest_word('люблю знают')}")
    if Longest_word('а б в г д') == 'а':
        print('+')
    else:
        print(f"Неверно, для строки 'а б в г д' ожидается 'а', а у вас {Longest_word('а б в г д')}")


test_task2()
stroka = str(input())
print(Longest_word(stroka))