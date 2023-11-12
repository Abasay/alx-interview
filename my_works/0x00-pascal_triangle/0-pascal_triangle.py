#!/usr/bin/python3
'''
Pascal triangle generator
'''


def factorial(n):
    '''factorial of each n integer value'''
    if n < 1:
        return 1
    return (int(n) * factorial(n - 1))


def comb(num, base):
    '''
       pascal triangle formula
       pascal values generator
    '''
    numerator = factorial(num)
    denominator = factorial(base)
    subtractFcto = factorial(num - base)

    return (numerator / (denominator * subtractFcto))


def pascal_row(num):
    '''
       generate pascal row for each number
    '''
    pascal_sub_list = []
    for j in range(0, num + 1):
        pascal_sub_list.append(int(comb(num, j)))

    return pascal_sub_list


def pascal_recursive(size, arr):
    '''generate triangle rows recursively'''
    pascal_triangle_list = arr
    if size < 1:
        return pascal_triangle_list
    pascal_triangle_list.append(pascal_row(size))
    return (pascal_recursive(size - 1, arr=pascal_triangle_list))


def pascal_triangle(num):
    ''' the pascal triangle'''
    if (num <= 0):
        return []
    triangle_list = pascal_recursive(num, [])
    extra_list = [[1]]
    newList = triangle_list[1:] + extra_list

    return newList[::-1]
