import math


def digital_root(num_1):
    while num_1 > 9:
        num_1 = sum(int(x) for x in str(num_1))
    return num_1


def factorial(num_1):
    if num_1 == 0 or num_1 == 1:
        return 1
    return num_1*factorial(num_1-1)


def sum_of_factors(num_1):
    curr_sum = 1
    temp = num_1
    for i in range(2, (num_1//2)+1):
        if num_1 % i == 0:
            temp = temp / i
            curr_sum += i
    return curr_sum


def count_prime_numbers(num_1):
    count = 0
    for i in range(2, num_1+1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            count += 1
    return count


def triangle_number(num_1):
    sum = 0
    if num_1 == 0:
        return sum
    for i in range(1, num_1+1):
        sum += i
    return sum+triangle_number(num_1-1)


def maximum_num(num_1):
    for i in range(0, 1):
        result = 0
        i = 1
        while num_1//i > 0:
            temp = (num_1 // (i * 10)) * i + (num_1 % i)
            i *= 10
            if temp > result:
                result = temp
    return result


def combinations(n, r):
    return factorial(n)//(factorial(r)*(factorial(n-r)))
