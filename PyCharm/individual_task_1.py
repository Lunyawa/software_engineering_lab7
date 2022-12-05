#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input("Введите список одной строкой").split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Сумма элементов меньшие 0 и кратные 7.
    s = ch = 0
    for i in A:
        if i < 0 and i % 7 == 0:
            ch += 1
            s += i

    # Вывод суммы и кол-во эелементов, которые отрицательные и кратные 7.
    print(f"Сумма = {s} \nКол-во эелементов = {ch}")