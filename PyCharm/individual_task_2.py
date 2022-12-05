#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    L = list(map(float, input("Введите список одной строкой: ").split()))
    # Ввод границ a и b.
    a, b = map(float, input("Введите границы a и b: ").split())

    # Если список пуст, завершить программу.
    if not L:
        print(
            "заданный список пуст",
            file=sys.stderr
        )
        exit(1)

    # Поиск максимального по модулю элемента и суммы элементов после 1-ого
    # положительного элемента.
    max_i = L[0]
    flag = s = 0
    for i in L:
        max_i = max(max_i, abs(i))
        if i > 0 or flag:
            flag = 1
            s += i

    # Создание нового списка, удоволетворяющего условие.
    new_L = [i for i in L if a <= i <= b] + [i for i in L if not (a <= i <= b)]

    print(f"Максимальный по модулю элемент -> {max_i}")
    print(f"Сумма элементов после 1-ого положительного эелемента -> {s}")
    print(f"Новый список -> {new_L}")
