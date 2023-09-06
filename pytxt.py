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

l3 = []
max_len = max(len(l1), len(l2))
min_len = min(len(l1), len(l2))

for i in range(max_len):
    sum_result = 0
    if i < min_len:
        sum_result = l1[i] + l2[i]
    elif len(l1) > len(l2):
        sum_result = l1[i]
    elif len(l2) > len(l1):
        sum_result = l2[i]

    if sum_result > 9:
        unit = sum_result % 10
        decade = sum_result // 10
        l3.append(unit)
        l3.append(decade)
    else:
        l3.append(sum_result)

print(l3)
