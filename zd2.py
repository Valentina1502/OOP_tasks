#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Реализация алгоритма Хаффмана
'''


def knapsack(cap, values, weights):
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            cap_left -= item['weight']
        elif cap_left > 0:
            total += item['vpw'] * cap_left
            cap_left = 0
    return total


if __name__ == '__main__':
    #Общая вместительность рюкзака
    cap = 40
    #Стоимость предметов
    values = [50, 75, 100]
    #соответствующие веса предметов
    weights = [10, 20, 15]
    print("Максимальная стоимость рюкзака составит: ", knapsack(cap, values, weights))
