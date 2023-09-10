import random

ask_user_1 = int(input('Введіть кількість елементів масиву 1: '))
ask_user_2 = int(input('Введіть кількість елементів масиву 2: '))

def fill_list_with_nums(L, len_list):
    while len(L) != len_list:
        L.append(random.randint(1, 9))

l1 = []
fill_list_with_nums(l1, ask_user_1)
print(l1)

l2 = []
fill_list_with_nums(l2, ask_user_2)
print(l2)

l1.reverse()
l2.reverse()

max_len = max(len(l1), len(l2))
min_len = min(len(l1), len(l2))

l3 = []
carry = 0

asking = input('Натисніть 1 для додавання або 2 для віднімання: ').strip()

match int(asking):
    case 1:
        for i in range(max_len):
            sum_result = 0
            if i < min_len:
                sum_result = l1[i] + l2[i] + carry
            elif len(l1) > len(l2):
                sum_result = l1[i] + carry
            elif len(l2) > len(l1):
                sum_result = l2[i] + carry

            carry = sum_result // 10
            sum_result = sum_result % 10
            l3.append(sum_result)

        if carry > 0:
            l3.append(carry)

    case 2:
        for i in range(max_len):
            diff_result = 0
            if i < min_len:
                diff_result = l1[i] - l2[i] - carry
            elif len(l1) > len(l2):
                diff_result = l1[i] - carry
            elif len(l2) > len(l1):
                diff_result = l2[i] - carry

            if diff_result < 0:
                carry = 1
                diff_result += 10
            else:
                carry = 0

            l3.append(diff_result)

        if carry > 0:
            l3.append(carry)

l3.reverse()
print(l3)
