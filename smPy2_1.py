# def avg_5(a, b, c, d):
#     return round((a + b + c + d) / 4, 5)
#
#
# print(avg_5(3.5, 2, 4.8, 2))


# def mul_to_int(a, b):
#     res = a * b
#     if float(res).is_integer():
#         return int(res)
#     return res
#
#
# print(mul_to_int(5, 4))

def round_standard(num):
    if num >= 0:
        sign = 1
    else:
        sign = -1
    return sign * int((abs(num) + 0.5))


# Тесты
print(round_standard(1.5))
print(round_standard(-2.5))
print(round_standard(1.6))
print(round_standard(5.11))
