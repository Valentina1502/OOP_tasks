#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Реализация задачи про максимальную стоимость предметов рюкзака
'''


def knapsack(bag, goods, weights):
    items = []
    for i, item in enumerate(goods):
        itemInfo = {
            'vpw': goods[i] / weights[i],
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
    bag_left = bag
    for item in items:
        if bag_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            bag_left -= item['weight']
        elif bag_left > 0:
            total += item['vpw'] * bag_left
            bag_left = 0
    return total


if __name__ == '__main__':
    bag = int(input("Вместимость рюкзака: "))
    goods = tuple(map(int, input("Введите соответствующую стоимость предметов:  ").split()))
    weights = tuple(map(int, input("Введите соответствующие веса предметов: ").split()))
    print("\nМаксимальная стоимость рюкзака составит: ", knapsack(bag, goods, weights))
