# def dislike_6(a):
#     if (type(a) is float or type(a) is int) and a == 6.0:
#         return 'Только не 6!'
#     return True
#
#
# print(dislike_6(5))
# print(dislike_6(6))


# def help_bool(letter=None):
#     if letter == 'к':
#         return 'A or B = B or A\nA and B = B and A'
#     elif letter == 'а':
#         return 'A or (B or C) == (A or B) or C == A or B or C\n' \
#                'A and (B and C) == (A and B) and C == A and B and C'
#     elif letter == 'д':
#         return 'A and (B or C) == (A and B) or (A and C) \nA or (B and C) == (A or B) and (A or C)'
#     elif letter == 'м':
#         return 'not(A or B) == not A and not B \nnot(A and B) == not A or not B\n'\
#                'not(A < B) == A >= B\nnot(not(A)) = A'
#     else:
#         return 'Возможные аргументы: к – Коммутативность, д – Дистрибутивность, а – Ассоциативность, ' \
#            'м – Теорема Де Моргана'
#
#
# # Тесты
# print(help_bool())
# print(help_bool([2, 6]))
# print(help_bool('а'))

# a = None
# if len(a) > 0 and a is not None:
#     print('OK')

# a = None
# if a is not None and len(a) > 0:
#     print('OK')

# def divider(a, b):
#     if b == 0:
#         return "Нули в знаменателе не приветствуются"
#     return (a * b) ** 2

def divider(a, b):
    result = b and (a / b) ** 3 or "Нули в знаменателе не приветствуются"
    return result


print(divider(4, 2))
